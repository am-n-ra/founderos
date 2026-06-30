
## 2026-06-30 — Bug CheckOutcome: WIN erroné quand SL touché

**Fichier**: ReversalDetector.mq5 (v5.20)
**Ligne**: ~155, fonction CheckOutcome()

**Symptôme**: Setup classé WIN alors que le SL a été touché.

**Cause**: Dans la boucle forward, TP était checké AVANT SL :
\\\mql5
if(bull) { if(bH >= tp) return  1; if(bL <= sl) return -1; }
\\\
Quand les deux niveaux étaient atteints sur la même bougie (SL 10pts + TP 34.1pts = haute volatilité), la fonction retournait toujours WIN car TP trouvé en premier.

**Fix**: Checker SL en premier (conservateur) :
\\\mql5
if(bull) { if(bL <= sl) return -1; if(bH >= tp) return  1; }
\\\

**Impact**: Les stats (WR, PF) étaient gonflées artificiellement. Le fix rend le classement strict : si SL touché ? LOSS, même si TP aussi atteint.
