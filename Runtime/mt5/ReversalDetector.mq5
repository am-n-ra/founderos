//+------------------------------------------------------------------+
//|                              ReversalDetector.mq5                 |
//|       6-Rule Reversal Setup Detector + Live Trading — MT5 M1     |
//+------------------------------------------------------------------+
//  REGLE 1 — Opposition   : B2 direction opposee a B1
//  REGLE 2 — Engulfing    : range B2 couvre entierement range B1
//  REGLE 3 — Sweep        : meche B2 depasse extreme B1 cote inverse
//  REGLE 4 — Price Gap    : B2 ouvre avec gap dans son sens vs cloture B1
//  REGLE 5 — Close        : B2 cloture au-dela de l'extreme B1
//  REGLE 6 — Exhaustion   : aucune des 3 bougies avant B1 ne depasse extreme B1
//+------------------------------------------------------------------+
#property copyright "FounderHQ"
#property version   "5.20"
#include <Trade\Trade.mqh>

//──────────────────────────────────────────────────────────────────
//  INPUTS
//──────────────────────────────────────────────────────────────────
input group "--- SCAN -------------------------------------------"
input int    LookbackBars   = 500;
input int    MaxSpreadPts   = 5;

input group "--- SL / TP ----------------------------------------"
input double SL_Points      = 10.0;
input double TP_Points      = 34.1;
input int    MaxBarsForward = 300;

input group "--- AFFICHAGE --------------------------------------"
input bool   ShowSLTP       = true;
input bool   ShowLabels     = true;
input int    LineBars       = 80;
input color  ColBull        = clrLime;
input color  ColBear        = clrRed;
input color  ColSL          = clrOrangeRed;
input color  ColTP          = clrDodgerBlue;

input group "--- DEBUG ------------------------------------------"
input bool   DebugMode      = false;

input group "--- OPTIMISATION SL/TP -----------------------------"
input bool   RunOptimize    = true;
input double SlMin          = 1.0;
input double SlMax          = 30.0;
input double SlStep         = 0.1;
input double TpMin          = 1.0;
input double TpMax          = 60.0;
input double TpStep         = 0.1;
input double MinWinRatePct  = 50.0;

input group "--- LIVE TRADING -----------------------------------"
input bool   LiveTrading      = false;
input double RiskPerTrade     = 0.10;
input int    MagicNumber      = 202606;
input bool   ClosePosOnDeinit = true;

input group "--- COMPOUNDING ------------------------------------"

//──────────────────────────────────────────────────────────────────
//  GLOBALS — SCAN / STATS
//──────────────────────────────────────────────────────────────────
int      g_count   = 0;
int      g_wins    = 0;
int      g_losses  = 0;
int      g_pending = 0;
datetime g_lastTime = 0;

//──────────────────────────────────────────────────────────────────
//  GLOBALS — TRADING
//──────────────────────────────────────────────────────────────────
CTrade   g_trade;
ulong    g_ticket       = 0;
datetime g_lastTradeBar = 0;

//──────────────────────────────────────────────────────────────────
//  GLOBALS — COMPOUNDING
//──────────────────────────────────────────────────────────────────
double   g_currentRisk    = 0.0;
double   g_balanceAtLevel = 0.0;
int      g_compoundLevel  = 1;

//──────────────────────────────────────────────────────────────────
//  GLOBALS — OPTIMISATION
//──────────────────────────────────────────────────────────────────
struct OptSetup {
   datetime time;
   double   entry;
   bool     bull;
   int      b2;
   int      fwdBars;
   double   fwdHigh[500];
   double   fwdLow[500];
};
OptSetup g_opt[1000];
int      g_optCount = 0;

//+------------------------------------------------------------------+
int OnInit()
{
   PrintFormat("=== ReversalDetector v5.20 | SL %.1fpts | TP %.1fpts | RR %.2f ===",
               SL_Points, TP_Points, TP_Points / SL_Points);

   g_currentRisk    = RiskPerTrade;
   g_balanceAtLevel = AccountInfoDouble(ACCOUNT_BALANCE);
   g_compoundLevel  = 1;
   PrintFormat("Compounding init: risque=$%.2f | balance=$%.2f | seuil=$%.2f",
               g_currentRisk, g_balanceAtLevel, g_currentRisk * 10.0);

   FullScan();

   if(LiveTrading)
   {
      g_trade.SetExpertMagicNumber(MagicNumber);
      g_trade.SetDeviationInPoints(5);
      double lot = CalcLot();
      PrintFormat("Mode LIVE | Risque: $%.2f/trade | Lot: %.2f | SL: %.1fpts | TP: %.1fpts",
                  g_currentRisk, lot, SL_Points, TP_Points);

      g_ticket = FindOpenPosition();
      if(g_ticket > 0)
         PrintFormat("Position existante reprise: ticket #%I64u", g_ticket);
   }
   return INIT_SUCCEEDED;
}

//+------------------------------------------------------------------+
void OnDeinit(const int reason)
{
   if(LiveTrading && ClosePosOnDeinit && g_ticket > 0)
   {
      if(PositionSelectByTicket(g_ticket))
         if((long)PositionGetInteger(POSITION_MAGIC) == MagicNumber)
            g_trade.PositionClose(_Symbol);
   }
   ObjectsDeleteAll(0, "REV_");
   ObjectsDeleteAll(0, "STP_");
   ChartRedraw(0);
}

//+------------------------------------------------------------------+
void OnTick()
{
   datetime t = iTime(_Symbol, PERIOD_M1, 0);
   if(t == g_lastTime) return;
   g_lastTime = t;

   if(LiveTrading)
   {
      if(g_ticket > 0 && !PositionSelectByTicket(g_ticket))
      {
         PrintFormat("Position #%I64u fermee. Verification compounding...", g_ticket);
         g_ticket = 0;
         CheckCompounding();
         FullScan();
      }
   }

   CheckBar(1);
   DrawStatsPanel();
   ChartRedraw(0);
}

//+------------------------------------------------------------------+
ulong FindOpenPosition()
{
   for(int i = PositionsTotal() - 1; i >= 0; i--)
   {
      ulong ticket = PositionGetTicket(i);
      if(ticket == 0) continue;
      if(PositionGetString(POSITION_SYMBOL)  == _Symbol &&
         (long)PositionGetInteger(POSITION_MAGIC) == MagicNumber)
         return ticket;
   }
   return 0;
}

//+------------------------------------------------------------------+
//| Calcule le lot a partir du risque courant en $                    |
//|   Formule : lot = risque_$ / (SL_en_points × tick_value)          |
//+------------------------------------------------------------------+
double CalcLot()
{
   double tickValue  = SymbolInfoDouble(_Symbol, SYMBOL_TRADE_TICK_VALUE);

   if(tickValue <= 0.0)
   {
      Print("WARN CalcLot: tickValue invalide, lot minimum utilise");
      return SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   }

   double slCostPerLot = SL_Points * tickValue;

   if(slCostPerLot <= 0.0)
   {
      Print("WARN CalcLot: slCostPerLot invalide, lot minimum utilise");
      return SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   }

   double lot = g_currentRisk / slCostPerLot;

   if(DebugMode)
      PrintFormat("CalcLot | tickVal=%.5f slPerLot=%.4f$ | lot=%.4f -> %.2f",
                  tickValue, slCostPerLot, lot, NormalizeLot(lot));

   return NormalizeLot(lot);
}

//+------------------------------------------------------------------+
double NormalizeLot(double lot)
{
   double minLot  = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   double maxLot  = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MAX);
   double stepLot = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_STEP);
   lot = MathRound(lot / stepLot) * stepLot;
   if(lot < minLot) lot = minLot;
   if(lot > maxLot) lot = maxLot;
   return lot;
}

//+------------------------------------------------------------------+
void CheckCompounding()
{
   double balance      = AccountInfoDouble(ACCOUNT_BALANCE);
   double profitLevel  = balance - g_balanceAtLevel;
   double threshold    = g_currentRisk * 10.0;

   if(profitLevel >= threshold)
   {
      double oldRisk   = g_currentRisk;
      g_currentRisk   *= 2.0;
      g_balanceAtLevel = balance;
      g_compoundLevel++;

      PrintFormat(">>> COMPOUNDING Level %d: risque $%.2f -> $%.2f (seuil $%.2f atteint | balance=$%.2f)",
                  g_compoundLevel, oldRisk, g_currentRisk, threshold, balance);
      PrintFormat(">>> Prochain seuil: $%.2f de profit pour passer a $%.2f",
                  g_currentRisk * 10.0, g_currentRisk * 2.0);
   }
}

//+------------------------------------------------------------------+
void FullScan()
{
   ObjectsDeleteAll(0, "REV_");
   ObjectsDeleteAll(0, "STP_");
   g_count = g_wins = g_losses = g_pending = 0;
   g_optCount = 0;

   int total = (int)Bars(_Symbol, PERIOD_M1);
   int start = (int)MathMin(LookbackBars + 5, total - 1);
   for(int i = start; i >= 2; i--)
      CheckBar(i);

   DrawStatsPanel();
   ChartRedraw(0);

   int resolved = g_wins + g_losses;
   double wr    = resolved > 0 ? 100.0 * g_wins / resolved : 0.0;
   double pf    = g_losses > 0 ? (g_wins * TP_Points) / (g_losses * SL_Points) : 0.0;
   PrintFormat("=== STATS | Total: %d | W: %d | L: %d | En cours: %d | WR: %.1f%% | PF: %.2f ===",
               g_count, g_wins, g_losses, g_pending, wr, pf);

   if(RunOptimize && g_optCount > 0)
      OptimizeSLTP();
}

//+------------------------------------------------------------------+
int CheckOutcome(int b2, bool bull, double sl, double tp)
{
   int total   = (int)Bars(_Symbol, PERIOD_M1);
   int scanEnd = MathMax(b2 - MaxBarsForward, 1);
   for(int k = b2 - 1; k >= scanEnd; k--)
   {
      if(k < 1 || k >= total) break;
      double bH = NormalizeDouble(iHigh(_Symbol, PERIOD_M1, k), _Digits);
      double bL = NormalizeDouble(iLow (_Symbol, PERIOD_M1, k), _Digits);
      if(bull) { if(bH >= tp) return  1; if(bL <= sl) return -1; }
      else     { if(bL <= tp) return  1; if(bH >= sl) return -1; }
   }
   return 0;
}

//+------------------------------------------------------------------+
void CheckBar(int b2)
{
   int total = (int)Bars(_Symbol, PERIOD_M1);
   if(b2 < 1 || b2 + 5 >= total) return;

   double B2o = NormalizeDouble(iOpen (_Symbol, PERIOD_M1, b2),     _Digits);
   double B2h = NormalizeDouble(iHigh (_Symbol, PERIOD_M1, b2),     _Digits);
   double B2l = NormalizeDouble(iLow  (_Symbol, PERIOD_M1, b2),     _Digits);
   double B2c = NormalizeDouble(iClose(_Symbol, PERIOD_M1, b2),     _Digits);
   datetime B2t = iTime(_Symbol, PERIOD_M1, b2);

   double B1o = NormalizeDouble(iOpen (_Symbol, PERIOD_M1, b2 + 1), _Digits);
   double B1h = NormalizeDouble(iHigh (_Symbol, PERIOD_M1, b2 + 1), _Digits);
   double B1l = NormalizeDouble(iLow  (_Symbol, PERIOD_M1, b2 + 1), _Digits);
   double B1c = NormalizeDouble(iClose(_Symbol, PERIOD_M1, b2 + 1), _Digits);

   if(MaxSpreadPts > 0 && b2 <= 3)
      if((int)SymbolInfoInteger(_Symbol, SYMBOL_SPREAD) > MaxSpreadPts) return;

   bool B1bull = (B1c > B1o);
   bool B1bear = (B1c < B1o);
   bool B2bull = (B2c > B2o);
   if(B2c == B2o)         return;
   if(B1bull && B2bull)   return;
   if(B1bear && !B2bull)  return;

   if(B2h < B1h || B2l > B1l)
   { if(DebugMode) PrintFormat("Bar %d: R2 FAIL", b2); return; }

   if( B2bull && B2l >= B1l) { if(DebugMode) PrintFormat("Bar %d: R3 FAIL sweep bas",  b2); return; }
   if(!B2bull && B2h <= B1h) { if(DebugMode) PrintFormat("Bar %d: R3 FAIL sweep haut", b2); return; }

   if( B2bull && B2o <= B1c) { if(DebugMode) PrintFormat("Bar %d: R4 FAIL gap haut", b2); return; }
   if(!B2bull && B2o >= B1c) { if(DebugMode) PrintFormat("Bar %d: R4 FAIL gap bas",  b2); return; }

   if( B2bull && B2c <= B1h) { if(DebugMode) PrintFormat("Bar %d: R5 FAIL close haut", b2); return; }
   if(!B2bull && B2c >= B1l) { if(DebugMode) PrintFormat("Bar %d: R5 FAIL close bas",  b2); return; }

   for(int j = 0; j < 3; j++)
   {
      double ph = NormalizeDouble(iHigh(_Symbol, PERIOD_M1, b2 + 2 + j), _Digits);
      double pl = NormalizeDouble(iLow (_Symbol, PERIOD_M1, b2 + 2 + j), _Digits);
      if( B2bull && pl < B1l) { if(DebugMode) PrintFormat("Bar %d: R6 FAIL haussier [%d]", b2, j); return; }
      if(!B2bull && ph > B1h) { if(DebugMode) PrintFormat("Bar %d: R6 FAIL baissier [%d]", b2, j); return; }
   }

   double entry = B2c;
   double sl = B2bull ? entry - SL_Points * _Point : entry + SL_Points * _Point;
   double tp = B2bull ? entry + TP_Points * _Point : entry - TP_Points * _Point;

   if(LiveTrading && b2 == 1 && g_ticket == 0 && B2t != g_lastTradeBar)
      TradeSetup(B2bull, entry, sl, tp, B2t);

   if(RunOptimize && g_optCount < 1000)
   {
      int idx = g_optCount;
      g_opt[idx].time  = B2t;
      g_opt[idx].entry = entry;
      g_opt[idx].bull  = B2bull;
      g_opt[idx].b2    = b2;
      int scanEnd = MathMax(b2 - MaxBarsForward, 1);
      int bars = 0;
      for(int k = b2 - 1; k >= scanEnd && bars < 500; k--, bars++)
      {
         g_opt[idx].fwdHigh[bars] = iHigh(_Symbol, PERIOD_M1, k);
         g_opt[idx].fwdLow[bars]  = iLow (_Symbol, PERIOD_M1, k);
      }
      g_opt[idx].fwdBars = bars;
      g_optCount++;
   }

   int outcome = CheckOutcome(b2, B2bull, sl, tp);
   g_count++;
   if     (outcome ==  1) g_wins++;
   else if(outcome == -1) g_losses++;
   else                   g_pending++;

   if(DebugMode)
      PrintFormat("Setup #%d %s @ %.5f | B2=%.1fpts | %s",
                  g_count, B2bull ? "BUY" : "SELL", entry, (B2h-B2l)/_Point,
                  outcome==1 ? "WIN" : outcome==-1 ? "LOSS" : "En cours");

   DrawSetup(g_count, B2t, entry, sl, tp, B2bull, outcome);
}

//+------------------------------------------------------------------+
void TradeSetup(bool bull, double entry, double sl, double tp, datetime barTime)
{
   double bid    = SymbolInfoDouble(_Symbol, SYMBOL_BID);
   double ask    = SymbolInfoDouble(_Symbol, SYMBOL_ASK);
   double spread = (ask - bid) / _Point;

   if(MaxSpreadPts > 0 && spread > MaxSpreadPts)
   {
      PrintFormat(">> SPREAD %.1fpts > %dpts — trade ignore", spread, MaxSpreadPts);
      return;
   }

   double lot = CalcLot();
   g_lastTradeBar = barTime;

   double slLive, tpLive;
   bool   ok = false;

   if(bull)
   {
      slLive = ask - SL_Points * _Point;
      tpLive = ask + TP_Points * _Point;
      PrintFormat(">> BUY  @ %.5f | SL %.5f (%.1fpts) | TP %.5f (%.1fpts) | Spread %.1fpts | Risque $%.2f | Lot %.2f",
                  ask, slLive, (ask-slLive)/_Point, tpLive, (tpLive-ask)/_Point, spread, g_currentRisk, lot);
      ok = g_trade.Buy(lot, _Symbol, ask, slLive, tpLive);
   }
   else
   {
      slLive = bid + SL_Points * _Point;
      tpLive = bid - TP_Points * _Point;
      PrintFormat(">> SELL @ %.5f | SL %.5f (%.1fpts) | TP %.5f (%.1fpts) | Spread %.1fpts | Risque $%.2f | Lot %.2f",
                  bid, slLive, (slLive-bid)/_Point, tpLive, (bid-tpLive)/_Point, spread, g_currentRisk, lot);
      ok = g_trade.Sell(lot, _Symbol, bid, slLive, tpLive);
   }

   if(ok)
   {
      g_ticket = g_trade.ResultOrder();
      PrintFormat(">> Trade ouvert | Ticket #%I64u | Lot %.2f | Risque $%.2f | Compounding Lvl %d",
                  g_ticket, lot, g_currentRisk, g_compoundLevel);
   }
   else
   {
      PrintFormat("ERREUR ouverture | Code: %d | %s", GetLastError(), g_trade.ResultComment());
      g_ticket = 0;
   }
}

//+------------------------------------------------------------------+
struct OptRank { double val; double sl; double tp; double wr; double pf; double ev; int w; int l; int n; };

void OptimizeSLTP()
{
   int slSteps  = (int)((SlMax - SlMin) / SlStep) + 1;
   int tpSteps  = (int)((TpMax - TpMin) / TpStep) + 1;
   int total    = slSteps * tpSteps;
   int normDec  = MathMax((int)(-MathFloor(MathLog10(SlStep)) + 0.5),
                           (int)(-MathFloor(MathLog10(TpStep)) + 0.5));
   double tol   = MathMin(SlStep, TpStep) / 2.0;

   OptRank best[10];
   for(int i = 0; i < 10; i++) best[i].val = -9999;

   PrintFormat("=== OPTIMISATION: %d setups x %d paires SL/TP ===", g_optCount, total);

   int tested = 0, pctProg = 0;
   for(int si = 0; si < slSteps; si++)
   for(int ti = 0; ti < tpSteps; ti++)
   {
      double slPts = NormalizeDouble(SlMin + si * SlStep, normDec);
      double tpPts = NormalizeDouble(TpMin + ti * TpStep, normDec);
      if(tpPts < slPts) continue;

      int wins = 0, losses = 0, pending = 0;
      double pt = _Point;
      for(int s = 0; s < g_optCount; s++)
      {
         double entry = g_opt[s].entry;
         bool   bull  = g_opt[s].bull;
         double sl    = bull ? entry - slPts * pt : entry + slPts * pt;
         double tp    = bull ? entry + tpPts * pt : entry - tpPts * pt;
         int    res   = 0;
         for(int k = 0; k < g_opt[s].fwdBars; k++)
         {
            double h = g_opt[s].fwdHigh[k];
            double l = g_opt[s].fwdLow[k];
            if(bull) { if(h >= tp) { res = 1; break; } if(l <= sl) { res = -1; break; } }
            else     { if(l <= tp) { res = 1; break; } if(h >= sl) { res = -1; break; } }
         }
         if(res == 1) wins++; else if(res == -1) losses++; else pending++;
      }
      tested++;

      int resolved = wins + losses;
      if(resolved == 0) continue;
      double wr  = 100.0 * wins / resolved;
      double pf  = losses > 0 ? (1.0 * wins * tpPts) / (losses * slPts) : 0.0;
      double ev  = (wr / 100.0) * tpPts - ((100.0 - wr) / 100.0) * slPts;
      double cmp = ev * (wr / 100.0) * pf;
      if(MinWinRatePct > 0 && wr < MinWinRatePct) continue;

      OptRank cur; cur.val=cmp; cur.sl=slPts; cur.tp=tpPts; cur.wr=wr; cur.pf=pf; cur.ev=ev; cur.w=wins; cur.l=losses; cur.n=resolved;
      bool dup = false;
      for(int d = 0; d < 10 && best[d].val > -9998; d++)
         if(MathAbs(best[d].sl-slPts) < tol && MathAbs(best[d].tp-tpPts) < tol) { dup = true; break; }
      if(dup) continue;
      for(int r = 0; r < 10; r++)
         if(cmp > best[r].val) { for(int z=9; z>r; z--) best[z]=best[z-1]; best[r]=cur; break; }

      int curPct = (int)(100.0 * tested / total);
      if(curPct >= pctProg + 10) { pctProg = curPct; PrintFormat("  %d/%d (%d%%)", tested, total, curPct); }
   }

   Print("=== TOP 10 par score EV x WR x PF ===");
   Print("  #  |  SL  |  TP  |  RR  |  W  |  L  |  WR%  |  PF  |  EV  | SCORE");
   Print("-----+------+------+------+-----+-----+-------+------+------+-------");
   for(int r = 0; r < 10 && best[r].val > -9998; r++)
      Print(StringFormat("  %2d | %5.2f| %5.2f| %5.2f| %3d | %3d | %5.1f | %5.2f| %5.1f| %6.2f",
                         r+1, best[r].sl, best[r].tp, best[r].tp/best[r].sl,
                         best[r].w, best[r].l, best[r].wr, best[r].pf, best[r].ev, best[r].val));
   Print("=== OPTIMISATION TERMINEE ===");
}

//+------------------------------------------------------------------+
void DrawSetup(int n, datetime t, double entry, double sl, double tp, bool bull, int outcome)
{
   string pfx  = "REV_" + IntegerToString(n) + "_";
   color  aCol = bull ? ColBull : ColBear;
   ObjArrow(pfx + "arr", t, entry, bull ? 233 : 234, aCol);
   if(ShowLabels)
   {
      string tag  = outcome== 1 ? " [W]" : outcome==-1 ? " [L]" : "";
      color  lCol = outcome== 1 ? clrAqua : outcome==-1 ? clrOrangeRed : aCol;
      ObjText(pfx+"lbl", t, bull ? entry-14*_Point : entry+14*_Point,
              StringFormat("#%d %s%s", n, bull?"BUY":"SELL", tag), lCol, 7);
   }
   if(ShowSLTP)
   {
      datetime t2 = t + (datetime)(LineBars * PeriodSeconds(PERIOD_M1));
      ObjTrend(pfx+"sl", t, sl, t2, sl, ColSL, STYLE_DOT);
      ObjTrend(pfx+"tp", t, tp, t2, tp, ColTP, STYLE_DOT);
   }
}

//+------------------------------------------------------------------+
void DrawStatsPanel()
{
   int    resolved = g_wins + g_losses;
   double wr       = resolved > 0 ? 100.0 * g_wins / resolved : 0.0;
   double pf       = g_losses > 0 ? (g_wins * TP_Points) / ((double)g_losses * SL_Points) : 0.0;
   double ev       = (wr/100.0)*TP_Points - ((100.0-wr)/100.0)*SL_Points;
   double beWR     = 100.0 * SL_Points / (SL_Points + TP_Points);

   double balance      = AccountInfoDouble(ACCOUNT_BALANCE);
   double profitLevel  = balance - g_balanceAtLevel;
   double threshold    = g_currentRisk * 10.0;
   double lot          = CalcLot();

   color wrCol = wr >= 60.0 ? clrLime : wr >= beWR ? clrYellow : clrOrangeRed;
   color pfCol = pf >= 2.0  ? clrLime : pf >= 1.0  ? clrYellow : clrOrangeRed;
   color prCol = profitLevel < 0               ? clrOrangeRed
               : profitLevel >= threshold*0.8  ? clrYellow
               :                                 clrSilver;

   struct R { string t; color c; };
   R rows[16];

   rows[0].t  = "== REVERSAL DETECTOR v5.20 =="; rows[0].c  = clrWhite;
   rows[1].t  = StringFormat("%-10s M1", _Symbol);              rows[1].c  = clrSilver;
   rows[2].t  = StringFormat("SL/TP     : %.1f / %.1f pts", SL_Points, TP_Points); rows[2].c = clrSilver;
   rows[3].t  = StringFormat("RR        : %.2f", TP_Points / SL_Points);           rows[3].c = clrSilver;
   rows[4].t  = "-----------------------------";                rows[4].c  = clrDimGray;
   rows[5].t  = StringFormat("Setups    : %d", g_count);        rows[5].c  = clrWhite;
   rows[6].t  = StringFormat("Wins      : %d", g_wins);         rows[6].c  = clrLime;
   rows[7].t  = StringFormat("Losses    : %d", g_losses);       rows[7].c  = clrOrangeRed;
   rows[8].t  = StringFormat("En cours  : %d", g_pending);      rows[8].c  = clrSilver;
   rows[9].t  = StringFormat("Win Rate  : %.1f%%  (BE:%.1f%%)", wr, beWR); rows[9].c = wrCol;
   rows[10].t = StringFormat("Prof.Fac  : %.2f   EV:%.1fpts", pf, ev);    rows[10].c = pfCol;
   rows[11].t = "-----------------------------";                 rows[11].c = clrDimGray;
   rows[12].t = StringFormat("Cpd Level : %d", g_compoundLevel);rows[12].c = clrYellow;
   rows[13].t = StringFormat("Risk/Trade: $%.2f  -> Lot: %.2f", g_currentRisk, lot); rows[13].c = clrWhite;
   rows[14].t = StringFormat("Seuil svt : $%.2f  -> $%.2f", threshold, g_currentRisk*2.0); rows[14].c = clrSilver;
   rows[15].t = StringFormat("Profit ici: $%.2f / $%.2f", profitLevel, threshold);  rows[15].c = prCol;

   for(int i = 0; i < 16; i++)
   {
      string name = "STP_" + IntegerToString(i);
      if(ObjectFind(0, name) < 0)
      {
         ObjectCreate(0, name, OBJ_LABEL, 0, 0, 0);
         ObjectSetInteger(0, name, OBJPROP_CORNER,    CORNER_RIGHT_UPPER);
         ObjectSetInteger(0, name, OBJPROP_XDISTANCE, 220);
         ObjectSetInteger(0, name, OBJPROP_YDISTANCE, 14 + i * 16);
         ObjectSetString (0, name, OBJPROP_FONT,      "Courier New");
         ObjectSetInteger(0, name, OBJPROP_FONTSIZE,  9);
         ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
         ObjectSetInteger(0, name, OBJPROP_HIDDEN,    true);
      }
      ObjectSetString (0, name, OBJPROP_TEXT,  rows[i].t);
      ObjectSetInteger(0, name, OBJPROP_COLOR, rows[i].c);
   }
}

//+------------------------------------------------------------------+
void ObjArrow(string n, datetime t, double y, int code, color c)
{
   ObjectCreate(0, n, OBJ_ARROW, 0, t, y);
   ObjectSetInteger(0, n, OBJPROP_ARROWCODE,  code);
   ObjectSetInteger(0, n, OBJPROP_COLOR,      c);
   ObjectSetInteger(0, n, OBJPROP_WIDTH,      2);
   ObjectSetInteger(0, n, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, n, OBJPROP_HIDDEN,     true);
}
void ObjText(string n, datetime t, double y, string txt, color c, int sz)
{
   ObjectCreate(0, n, OBJ_TEXT, 0, t, y);
   ObjectSetString (0, n, OBJPROP_TEXT,       txt);
   ObjectSetInteger(0, n, OBJPROP_COLOR,      c);
   ObjectSetInteger(0, n, OBJPROP_FONTSIZE,   sz);
   ObjectSetInteger(0, n, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, n, OBJPROP_HIDDEN,     true);
}
void ObjTrend(string n, datetime t1, double y1, datetime t2, double y2, color c, int style)
{
   ObjectCreate(0, n, OBJ_TREND, 0, t1, y1, t2, y2);
   ObjectSetInteger(0, n, OBJPROP_COLOR,      c);
   ObjectSetInteger(0, n, OBJPROP_STYLE,      style);
   ObjectSetInteger(0, n, OBJPROP_WIDTH,      1);
   ObjectSetInteger(0, n, OBJPROP_RAY_RIGHT,  false);
   ObjectSetInteger(0, n, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, n, OBJPROP_HIDDEN,     true);
}
//+------------------------------------------------------------------+
