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
#property version   "5.10"
#include <Trade\Trade.mqh>

//──────────────────────────────────────────────────────────────────
//  INPUTS
//──────────────────────────────────────────────────────────────────
input group "--- SCAN -------------------------------------------"
input int    LookbackBars   = 500;
input int    MaxSpreadPts   = 1;

input group "--- SL / TP ----------------------------------------"
input double SL_Points      = 10.0;
input double TP_Points      = 34.1;
input int    MaxBarsForward = 300;    // Barres max pour detecter le resultat W/L

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
input bool   RunOptimize    = true;    // Optimiser SL/TP apres scan
input double SlMin          = 1.0;     // SL minimum (points)
input double SlMax          = 30.0;    // SL maximum (points)
input double SlStep         = 0.1;     // Pas SL
input double TpMin          = 1.0;     // TP minimum (points)
input double TpMax          = 60.0;    // TP maximum (points)
input double TpStep         = 0.1;     // Pas TP
input double MinWinRatePct  = 50.0;    // WR% minimum pour etre rapportee (0=desactive)

input group "--- LIVE TRADING -----------------------------------"
input bool   LiveTrading    = false;   // Activer trading en direct
input double RiskPerTrade   = 0.5;     // Risque en $ par trade
input int    MagicNumber    = 202606;  // Magic number EA
input bool   ClosePosOnDeinit = true; // Fermer position a la suppression EA

//──────────────────────────────────────────────────────────────────
//  GLOBALS
//──────────────────────────────────────────────────────────────────
int      g_count   = 0;
int      g_wins    = 0;
int      g_losses  = 0;
int      g_pending = 0;
datetime g_lastTime = 0;

//--- Stockage pour optimisation
struct OptSetup {
   datetime time;
   double   entry;
   bool     bull;
   int      b2;
   int      fwdBars;
   double   fwdHigh[500];
   double   fwdLow[500];
};
OptSetup g_opt[1000];   // jusqu'a 1000 setups
int       g_optCount = 0;

//--- Trading
CTrade   g_trade;
datetime g_lastTradeBar = 0;    // Timestamp de la derniere barre tradee
int      g_ticket       = 0;    // Ticket de la position ouverte

//+------------------------------------------------------------------+
int OnInit()
{
   PrintFormat("=== ReversalDetector v5 | SL %.1fpts | TP %.1fpts | RR %.2f ===",
               SL_Points, TP_Points, TP_Points / SL_Points);
   FullScan();

   if(LiveTrading)
   {
      g_trade.SetExpertMagicNumber(MagicNumber);
      g_trade.SetDeviationInPoints(5);
      Print("Mode LIVE active. Risque: $", RiskPerTrade, " par trade (SL=", SL_Points, "pts)");

      //--- Check for existing position
      if(PositionSelect(_Symbol))
      {
         g_ticket = (int)PositionGetInteger(POSITION_TICKET);
         Print("Position existante reprise: ticket #", g_ticket);
      }
   }

   return INIT_SUCCEEDED;
}

void OnDeinit(const int reason)
{
   if(LiveTrading && ClosePosOnDeinit && PositionSelect(_Symbol))
   {
      if((int)PositionGetInteger(POSITION_MAGIC) == MagicNumber)
         g_trade.PositionClose(_Symbol);
   }

   ObjectsDeleteAll(0, "REV_");
   ObjectsDeleteAll(0, "STP_");
   ChartRedraw(0);
}

void OnTick()
{
   datetime t = iTime(_Symbol, PERIOD_M1, 0);
   if(t == g_lastTime) return;
   g_lastTime = t;

   //--- Si mode trading: verifier si la position est encore ouverte
   if(LiveTrading && g_ticket > 0)
   {
      if(!PositionSelectByTicket(g_ticket))
      {
         //--- Position fermee → compter le resultat dans les stats
         g_ticket = 0;
         Print("Position #", g_ticket, " fermee. Re-scan pour mise a jour stats...");
         FullScan();
      }
   }

   CheckBar(1);
   DrawStatsPanel();
   ChartRedraw(0);
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
//| CheckOutcome : regarde barre par barre ce qui a ete touche en 1er |
//| b2     = index de B2 (MT5 : 0=actuel, plus grand = plus ancien)   |
//| Retourne : 1=Win(TP) | -1=Loss(SL) | 0=En cours                  |
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

      if(bull)
      {
         if(bH >= tp) return  1;   // TP touche -> WIN
         if(bL <= sl) return -1;   // SL touche -> LOSS
      }
      else
      {
         if(bL <= tp) return  1;   // TP touche -> WIN
         if(bH >= sl) return -1;   // SL touche -> LOSS
      }
   }
   return 0;
}

//+------------------------------------------------------------------+
//| Moteur de detection des 6 regles                                   |
//+------------------------------------------------------------------+
void CheckBar(int b2)
{
   int total = (int)Bars(_Symbol, PERIOD_M1);
   if(b2 < 1 || b2 + 5 >= total) return;

   //--- Prix B2 et B1
   double B2o = NormalizeDouble(iOpen (_Symbol, PERIOD_M1, b2),     _Digits);
   double B2h = NormalizeDouble(iHigh (_Symbol, PERIOD_M1, b2),     _Digits);
   double B2l = NormalizeDouble(iLow  (_Symbol, PERIOD_M1, b2),     _Digits);
   double B2c = NormalizeDouble(iClose(_Symbol, PERIOD_M1, b2),     _Digits);
   datetime B2t = iTime(_Symbol, PERIOD_M1, b2);

   double B1o = NormalizeDouble(iOpen (_Symbol, PERIOD_M1, b2 + 1), _Digits);
   double B1h = NormalizeDouble(iHigh (_Symbol, PERIOD_M1, b2 + 1), _Digits);
   double B1l = NormalizeDouble(iLow  (_Symbol, PERIOD_M1, b2 + 1), _Digits);
   double B1c = NormalizeDouble(iClose(_Symbol, PERIOD_M1, b2 + 1), _Digits);

   //--- Filtre spread (bars recents seulement, historique pas dispo)
   if(MaxSpreadPts > 0 && b2 <= 3)
      if((int)SymbolInfoInteger(_Symbol, SYMBOL_SPREAD) > MaxSpreadPts) return;

   //--- R1 : Opposition (doji B1 accepte)
   bool B1bull = (B1c > B1o);
   bool B1bear = (B1c < B1o);
   bool B2bull = (B2c > B2o);
   if(B2c == B2o)              return;  // B2 doit avoir un sens clair
   if(B1bull && B2bull)        return;  // Les deux haussieres -> invalide
   if(B1bear && !B2bull)       return;  // Les deux baissieres -> invalide
   // B1 doji (ni B1bull ni B1bear) -> accepte tout sens de B2

   //--- R2 : Engulfing
   if(B2h < B1h || B2l > B1l)
   { if(DebugMode) PrintFormat("Bar %d: R2 FAIL", b2); return; }

   //--- R3 : Sweep
   if( B2bull && B2l >= B1l) { if(DebugMode) PrintFormat("Bar %d: R3 FAIL sweep bas",  b2); return; }
   if(!B2bull && B2h <= B1h) { if(DebugMode) PrintFormat("Bar %d: R3 FAIL sweep haut", b2); return; }

   //--- R4 : Price Gap
   if( B2bull && B2o <= B1c) { if(DebugMode) PrintFormat("Bar %d: R4 FAIL gap haut", b2); return; }
   if(!B2bull && B2o >= B1c) { if(DebugMode) PrintFormat("Bar %d: R4 FAIL gap bas",  b2); return; }

   //--- R5 : Cloture confirmatrice
   if( B2bull && B2c <= B1h) { if(DebugMode) PrintFormat("Bar %d: R5 FAIL close haut", b2); return; }
   if(!B2bull && B2c >= B1l) { if(DebugMode) PrintFormat("Bar %d: R5 FAIL close bas",  b2); return; }

   //--- R6 : Exhaustion (3 bougies avant B1)
   for(int j = 0; j < 3; j++)
   {
      double ph = NormalizeDouble(iHigh(_Symbol, PERIOD_M1, b2 + 2 + j), _Digits);
      double pl = NormalizeDouble(iLow (_Symbol, PERIOD_M1, b2 + 2 + j), _Digits);
      if( B2bull && pl < B1l) { if(DebugMode) PrintFormat("Bar %d: R6 FAIL haussier [%d]", b2, j); return; }
      if(!B2bull && ph > B1h) { if(DebugMode) PrintFormat("Bar %d: R6 FAIL baissier [%d]", b2, j); return; }
   }

   //--- Toutes les regles passees
   double entry = B2c;
   double sl = B2bull ? entry - SL_Points * _Point : entry + SL_Points * _Point;
   double tp = B2bull ? entry + TP_Points * _Point : entry - TP_Points * _Point;

   //--- Trading en direct si setup frais sur barre completee
   if(LiveTrading && b2 == 1 && g_ticket == 0 && B2t != g_lastTradeBar)
      TradeSetup(B2bull, entry, sl, tp, B2t);

   //--- Stockage pour optimisation SL/TP
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
         g_opt[idx].fwdLow[bars]  = iLow(_Symbol, PERIOD_M1, k);
      }
      g_opt[idx].fwdBars = bars;
      g_optCount++;
   }

   int outcome = CheckOutcome(b2, B2bull, sl, tp);

   g_count++;
   if     (outcome ==  1) g_wins++;
   else if(outcome == -1) g_losses++;
   else                   g_pending++;

   string oStr = (outcome == 1) ? "WIN" : (outcome == -1) ? "LOSS" : "En cours";
   if(DebugMode)
      PrintFormat("Setup #%d %s @ %.5f | B2=%.1fpts | %s",
                  g_count, B2bull ? "BUY" : "SELL",
                  entry, (B2h - B2l) / _Point, oStr);

   DrawSetup(g_count, B2t, entry, sl, tp, B2bull, outcome);
}

struct OptRank { double val; double sl; double tp; double wr; double pf; double ev; int w; int l; int n; };

//+------------------------------------------------------------------+
//| Optimise SL/TP : top 10 par score composite EV x WR x PF         |
//+------------------------------------------------------------------+
void OptimizeSLTP()
{
   int    slSteps = (int)((SlMax - SlMin) / SlStep) + 1;
   int    tpSteps = (int)((TpMax - TpMin) / TpStep) + 1;
   int    total   = slSteps * tpSteps;

   int    slDec   = MathMax(0, (int)(-MathFloor(MathLog10(SlStep)) + 0.5));
   int    tpDec   = MathMax(0, (int)(-MathFloor(MathLog10(TpStep)) + 0.5));
   int    normDec = MathMax(slDec, tpDec);
   double tol     = MathMin(SlStep, TpStep) / 2.0;

   OptRank best[10];
   for(int i = 0; i < 10; i++) best[i].val = -9999;

   PrintFormat("=== OPTIMISATION: %d setups x %d paires SL/TP (%d SL x %d TP) ===",
               g_optCount, total, slSteps, tpSteps);
   Print("Scanning...");

   int tested = 0;
   int pctProg = 0;
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

            if(bull)
            {
               if(h >= tp) { res = 1; break; }
               if(l <= sl) { res = -1; break; }
            }
            else
            {
               if(l <= tp) { res = 1; break; }
               if(h >= sl) { res = -1; break; }
            }
         }

         if     (res == 1) wins++;
         else if(res == -1) losses++;
         else              pending++;
      }

      tested++;
      int resolved = wins + losses;
      if(resolved == 0) continue;

      double wr  = 100.0 * wins / resolved;
      double pf  = losses > 0 ? (1.0 * wins * tpPts) / (losses * slPts) : 0.0;
      double ev  = (wr / 100.0) * tpPts - ((100.0 - wr) / 100.0) * slPts;
      double cmp = ev * (wr / 100.0) * pf;  // Composite: maximise EV x WR x PF

      if(MinWinRatePct > 0 && wr < MinWinRatePct) continue;

      OptRank cur; cur.val = cmp; cur.sl = slPts; cur.tp = tpPts; cur.wr = wr; cur.pf = pf; cur.ev = ev; cur.w = wins; cur.l = losses; cur.n = resolved;

      //--- Dedup: skip if same SL/TP already in top 10
      bool dup = false;
      for(int d = 0; d < 10 && best[d].val > -9998; d++)
         if(MathAbs(best[d].sl - slPts) < tol && MathAbs(best[d].tp - tpPts) < tol) { dup = true; break; }
      if(dup) continue;

      for(int r = 0; r < 10; r++)
      {
         if(cmp > best[r].val)
         {
            for(int z = 9; z > r; z--) best[z] = best[z-1];
            best[r] = cur;
            break;
         }
      }

      int curPct = (int)(100.0 * tested / total);
      if(curPct >= pctProg + 10) { pctProg = curPct; PrintFormat("  Progression: %d/%d (%d%%)", tested, total, curPct); }
   }

   Print(StringFormat("=== TOP 10 par score composite EV x WR x PF (sur %d paires, filtre WR>=%.0f%%) ===", tested, MinWinRatePct));
   Print("  #  |  SL  |  TP  |  RR  |  W  |  L  |  WR%%  |  PF  |  EV  | COMPO");
   Print("-----+------+------+------+-----+-----+-------+------+------+------");
   for(int r = 0; r < 10 && best[r].val > -9998; r++)
   {
      double rr = best[r].tp / best[r].sl;
      Print(StringFormat("  %2d | %5.4f| %5.4f| %5.2f| %3d | %3d | %5.1f | %5.2f| %5.1f| %5.1f",
                         r+1, best[r].sl, best[r].tp, rr, best[r].w, best[r].l, best[r].wr, best[r].pf, best[r].ev, best[r].val));
   }
   Print("=== OPTIMISATION TERMINEE ===");
}

//+------------------------------------------------------------------+
//| TradeSetup : ouvre une position en direct                        |
//+------------------------------------------------------------------+
double NormalizeLot(double lot)
{
   double min = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   double max = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MAX);
   double step = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_STEP);
   lot = MathRound(lot / step) * step;
   if(lot < min) lot = min;
   if(lot > max) lot = max;
   return lot;
}

void TradeSetup(bool bull, double entry, double sl, double tp, datetime barTime)
{
   double bid = SymbolInfoDouble(_Symbol, SYMBOL_BID);
   double ask = SymbolInfoDouble(_Symbol, SYMBOL_ASK);
   double spread = (ask - bid) / _Point;

   //--- Spread guard: pas de trade si spread > max autorise
   if(MaxSpreadPts > 0 && spread > MaxSpreadPts)
   {
      PrintFormat(">> SPREAD TROP ELEVE: %.1fpts > %dpts — trade skipped", spread, MaxSpreadPts);
      return;
   }

   double tickVal = SymbolInfoDouble(_Symbol, SYMBOL_TRADE_TICK_VALUE);
   double tickSize = SymbolInfoDouble(_Symbol, SYMBOL_TRADE_TICK_SIZE);
   double riskPerLot = SL_Points * (_Point / tickSize) * tickVal;
   if(riskPerLot <= 0) return;

   double lot = NormalizeLot(RiskPerTrade / riskPerLot);
   g_lastTradeBar = barTime;

   //--- SL/TP ajustes au spread actuel
   double slLive, tpLive;
   if(bull)
   {
      slLive = bid - SL_Points * _Point;
      tpLive = bid + TP_Points * _Point;
      PrintFormat(">> BUY @ %.5f | SL=%.5f (%.1fpts) TP=%.5f (%.1fpts) | Spread=%.1fpts | Lot=%.2f",
                  ask, slLive, (ask - slLive)/_Point, tpLive, (tpLive - ask)/_Point, spread, lot);
      g_ticket = g_trade.Buy(lot, _Symbol, ask, slLive, tpLive);
   }
   else
   {
      slLive = ask + SL_Points * _Point;
      tpLive = ask - TP_Points * _Point;
      PrintFormat(">> SELL @ %.5f | SL=%.5f (%.1fpts) TP=%.5f (%.1fpts) | Spread=%.1fpts | Lot=%.2f",
                  bid, slLive, (slLive - bid)/_Point, tpLive, (bid - tpLive)/_Point, spread, lot);
      g_ticket = g_trade.Sell(lot, _Symbol, bid, slLive, tpLive);
   }

   if(g_ticket > 0)
      PrintFormat(">> TRADE #%d ouverte", g_ticket);
   else
   {
      Print("ERREUR ouverture position: ", GetLastError());
      g_ticket = 0;
   }
}

//+------------------------------------------------------------------+
//| Dessin du setup avec couleur selon resultat                        |
//+------------------------------------------------------------------+
void DrawSetup(int n, datetime t, double entry, double sl, double tp,
               bool bull, int outcome)
{
   string pfx  = "REV_" + IntegerToString(n) + "_";
   color  aCol = bull ? ColBull : ColBear;

   ObjArrow(pfx + "arr", t, entry, bull ? 233 : 234, aCol);

   if(ShowLabels)
   {
      string tag  = (outcome ==  1) ? " [W]"
                  : (outcome == -1) ? " [L]" : "";
      color  lCol = (outcome ==  1) ? clrAqua
                  : (outcome == -1) ? clrOrangeRed : aCol;
      string txt  = StringFormat("#%d %s%s", n, bull ? "BUY" : "SELL", tag);
      ObjText(pfx + "lbl", t, bull ? entry - 14*_Point : entry + 14*_Point, txt, lCol, 7);
   }

   if(ShowSLTP)
   {
      datetime t2 = t + (datetime)(LineBars * PeriodSeconds(PERIOD_M1));
      ObjTrend(pfx + "sl", t, sl, t2, sl, ColSL, STYLE_DOT);
      ObjTrend(pfx + "tp", t, tp, t2, tp, ColTP, STYLE_DOT);
   }
}

//+------------------------------------------------------------------+
//| Panneau de statistiques - coin superieur droit                     |
//+------------------------------------------------------------------+
void DrawStatsPanel()
{
   int    resolved = g_wins + g_losses;
   double wr       = resolved > 0 ? 100.0 * g_wins  / resolved  : 0.0;
   double pf       = g_losses > 0 ? (g_wins * TP_Points) / ((double)g_losses * SL_Points) : 0.0;
   double ev       = (wr / 100.0) * TP_Points - ((100.0 - wr) / 100.0) * SL_Points;
   double beWR     = 100.0 * SL_Points / (SL_Points + TP_Points);

   color wrCol = (wr >= 60.0)  ? clrLime
               : (wr >= beWR)  ? clrYellow
               :                 clrOrangeRed;

   color pfCol = (pf >= 2.0)   ? clrLime
               : (pf >= 1.0)   ? clrYellow
               :                 clrOrangeRed;

   struct PanelLine { string text; color col; };
   PanelLine rows[11];

   rows[0].text  = "== REVERSAL DETECTOR v5 ==";  rows[0].col = clrWhite;
   rows[1].text  = StringFormat("Paire     :  %s M1", _Symbol);      rows[1].col = clrSilver;
   rows[2].text  = StringFormat("SL / TP   :  %.1f / %.1f pts", SL_Points, TP_Points); rows[2].col = clrSilver;
   rows[3].text  = StringFormat("RR        :  %.2f", TP_Points / SL_Points);           rows[3].col = clrSilver;
   rows[4].text  = "--------------------------";   rows[4].col = clrDimGray;
   rows[5].text  = StringFormat("Setups    :  %d", g_count);          rows[5].col = clrWhite;
   rows[6].text  = StringFormat("Wins      :  %d", g_wins);           rows[6].col = clrLime;
   rows[7].text  = StringFormat("Losses    :  %d", g_losses);         rows[7].col = clrOrangeRed;
   rows[8].text  = StringFormat("En cours  :  %d", g_pending);        rows[8].col = clrSilver;
   rows[9].text  = StringFormat("Win Rate  :  %.1f%%  (BE: %.1f%%)", wr, beWR); rows[9].col = wrCol;
   rows[10].text = StringFormat("Prof.Fac  :  %.2f   EV: %.1fpts", pf, ev);     rows[10].col = pfCol;

   for(int i = 0; i < 11; i++)
   {
      string name = "STP_" + IntegerToString(i);

      if(ObjectFind(0, name) < 0)
      {
         ObjectCreate(0, name, OBJ_LABEL, 0, 0, 0);
         ObjectSetInteger(0, name, OBJPROP_CORNER,     CORNER_RIGHT_UPPER);
         ObjectSetInteger(0, name, OBJPROP_XDISTANCE,  210);
         ObjectSetInteger(0, name, OBJPROP_YDISTANCE,  14 + i * 16);
         ObjectSetString (0, name, OBJPROP_FONT,       "Courier New");
         ObjectSetInteger(0, name, OBJPROP_FONTSIZE,   9);
         ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
         ObjectSetInteger(0, name, OBJPROP_HIDDEN,     true);
      }
      ObjectSetString (0, name, OBJPROP_TEXT,  rows[i].text);
      ObjectSetInteger(0, name, OBJPROP_COLOR, rows[i].col);
   }
}

//+------------------------------------------------------------------+
//  HELPERS
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
