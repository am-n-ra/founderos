# Déploiement EA ReversalDetector sur VPS Oracle Cloud (Gratuit)

## 1. Créer le compte Oracle Cloud

1. Va sur https://signup.cloud.oracle.com
2. Renseigne email, pays (Togo), numéro de téléphone
3. Ajoute une carte bancaire (pour vérification, rien n'est débité sur Always Free)
4. Confirme le code par SMS

## 2. Créer une instance Windows

1. Connecte-toi à https://cloud.oracle.com
2. Menu hamburger → Compute → Instances
3. Clique "Create instance"
4. **Name:** `mt5-ea`
5. **Placement:** laisser par défaut
6. **Image:** Change → "Windows", choisis **Windows Server 2022 Standard**
7. **Shape:** "Specialty and legacy" → **VM.Standard.E2.1.Micro** (Always Free eligible, 1 OCPU, 8GB RAM)
   - Si pas dispo, essaie **VM.Standard.A1.Flex** avec 1 OCPU (Always Free)
8. **Boot volume:** laisser par défaut (50GB Always Free)
9. **SSH keys:** laisser vide (on utilisera le mot de passe admin Windows)
10. **Create** → attendre que l'instance passe "Running" (5-10 min)

## 3. Se connecter à l'instance Windows

1. Une fois Running, clique sur le nom de l'instance
2. Sous "Instance access", clique **"Copy initial password"**
3. Télécharge le fichier RDP : clique **"Console connection"** → **"Create RDP connection"** → télécharge le `.rdp`
4. Ouvre le fichier `.rdp` téléchargé
5. Connecte-toi avec username `opc` et le mot de passe copié
6. Windows va demander de changer le mot de passe à la première connexion

## 4. Installer MetaTrader 5

1. Dans le VPS, ouvre Edge (ou Chrome via `chrome.google.com`)
2. Va sur https://www.metatrader5.com/en/download
3. Télécharge et installe MetaTrader 5
4. Ouvre MT5 → **File → Login to Trade Account**
5. Entre les identifiants Next Instant (serveur, login, mot de passe)

## 5. Déployer l'EA

1. Récupère le fichier `ReversalDetector.mq5` (depuis GitHub ou ton PC)
2. Dans MT5 : **File → Open Data Folder**
3. Navigue vers `MQL5\Experts\`
4. Copie `ReversalDetector.mq5` dans ce dossier
5. Dans MT5 : **Tools → MetaQuotes Language Editor** (F4)
6. Dans l'éditeur : ouvre le fichier depuis `MQL5/Experts/`
7. Appuie sur **F7** pour compiler (ou bouton "Compile")
8. Vérifie qu'il n'y a pas d'erreurs dans le terminal

## 6. Attacher l'EA au chart

1. **View → Market Watch** (Ctrl+M)
2. Clique droit sur EURUSD → **Chart Window**
3. Passe en timeframe M1
4. **Charts → Indicators List** → onglet **Expert Advisors**
5. Sélectionne `ReversalDetector` → clique **Attach**

## 7. Configurer les paramètres (copie exacte)

```
--- SCAN ---
LookbackBars   = 500
MaxSpreadPts   = 1

--- SL / TP ---
SL_Points      = 1.0
TP_Points      = 3.0
MaxBarsForward = 300

--- AFFICHAGE ---
(laisser par défaut)

--- DEBUG ---
DebugMode      = false

--- OPTIMISATION SL/TP ---
RunOptimize    = false      ← DÉSACTIVER sur le live
(laisser reste par défaut)

--- LIVE TRADING ---
LiveTrading    = true       ← ACTIVER
RiskPerTrade   = 0.5        (ou 1.0 si tu veux doubler)
MagicNumber    = 202606
ClosePosOnDeinit = false    ← GARDER FALSE (sécurité)
```

## 8. Vérifier que ça tourne

1. L'onglet "Experts" du Terminal doit afficher :
   ```
   === ReversalDetector v5 | SL 1.0pts | TP 3.0pts | RR 3.00 ===
   === STATS | Total: 348 | W: 210 | L: 136 | WR: 60.7% | PF: 6.17 ===
   Mode LIVE active. Risque: $0.5 par trade
   ```
2. Attends la prochaine bougie M1 (max 60 sec). À chaque setup détecté :
   ```
   >> BUY @ 1.xxxxx | SL=... (1.0pts) TP=... (3.0pts) | Spread=0.5pts | Lot=0.50
   >> TRADE #123456 ouverte
   ```

## 9. Garder la session ouverte 24/7

Oracle Cloud ferme la session RDP après déconnexion. Pour que MT5 reste ouvert :

1. Dans le VPS, crée un fichier `start_ea.bat` sur le bureau avec :
   ```batch
   @echo off
   start "" "C:\Program Files\MetaTrader 5\terminal64.exe"
   ```
2. **Option A — Tâche planifiée Windows :**
   - Tape "Task Scheduler" dans le menu démarrer
   - Crée une tâche : au démarrage du système → lancer `start_ea.bat`
   - Coche "Run whether user is logged on or not"
   
3. **Option B — Connexion automatique :**
   - Tape `netplwiz` → décoche "Users must enter password"
   - Sélectionne `opc` → entre le mot de passe
   - Redémarre → Windows démarre et MT5 s'ouvre automatiquement

## 10. Surveiller depuis ton PC

- Installe MT5 sur ton PC
- Connecte-toi au même compte Next Instant
- Tu verras les trades en temps réel dans le terminal
- Les transactions sont enregistrées côté broker, pas besoin que ton PC tourne

## Configuration VPS Oracle — Ubuntu + Wine (Gratuit)

Les images Windows Oracle sont payantes. Ubuntu + Wine = la solution 100% gratuite.

### A. Créer l'instance Ubuntu

1. Sur l'écran de sélection d'image, choisis **Canonical Ubuntu 24.04** (ou 22.04)
2. **Shape:** `VM.Standard.A1.Flex` (Always Free ARM)
3. Configure **1 OCPU**, **6 GB RAM**, **Boot volume 40 GB**
4. **SSH keys:** Télécharge la clé privée (ou colle ta clé publique)
5. **Create**

### B. Se connecter en SSH

Depuis Windows (PowerShell) ou Linux :

```bash
ssh -i oracle.key ubuntu@<IP_PUBLIQUE>
```

L'IP est dans les détails de l'instance après création.

### C. Installer Wine + MT5

```bash
# Mise à jour
sudo apt update && sudo apt upgrade -y

# Installation Wine + bureau distant
sudo dpkg --add-architecture i386
sudo apt install -y wine64 wine32 xfce4 xrdp

# Config RDP (bureau distant)
sudo systemctl enable xrdp
sudo systemctl start xrdp

# Télécharger MT5
cd ~
wget https://download.metatrader5.com/terminal/terminal64.exe

# Lancer MT5 avec Wine (interface graphique)
wine terminal64.exe
```

### D. Se connecter au bureau Ubuntu

1. Depuis Windows : **Démarrer → "Connexion Bureau à distance"** (mstsc)
2. Entrez l'IP publique de ton instance Ubuntu
3. Login : `ubuntu` + mot de passe (ou clé SSH)

### E. Configurer MT5 + EA

1. Dans le bureau Ubuntu : MT5 s'ouvre via Wine
2. **File → Login to Trade Account** → identifiants Next Instant
3. Copie `ReversalDetector.mq5` sur le bureau Ubuntu :
   ```bash
   scp ReversalDetector.mq5 ubuntu@<IP>:
   ```
4. Dans MT5 : **File → Open Data Folder** → navigue vers `drive_c/users/ubuntu/AppData/Roaming/MetaQuotes/Terminal/.../MQL5/Experts/`
5. Copie le fichier `.mq5` dedans
6. Compile F7 dans MetaEditor
7. Attache à EURUSD M1 mêmes paramètres que section 7

### F. Garder MT5 ouvert 24/7

```bash
# Option screen (déconnecte-toi sans tuer MT5)
sudo apt install -y screen
screen -S mt5
wine ~/.wine/drive_c/Program\ Files/MetaTrader\ 5/terminal64.exe
# Ctrl+A puis D pour détacher
# screen -r mt5 pour revenir
```

### G. Alternative sans bureau (headless)

Si tu ne peux pas RDP, MT5 peut tourner avec `xvfb` :

```bash
sudo apt install -y xvfb
xvfb-run wine terminal64.exe
```

## Rappel important

- **Ne touche pas aux trades ouverts manuellement** — laisse l'EA gérer SL/TP
- **Vérifie le journal Experts 1×/jour** au début pour confirmer que l'EA tourne et ouvre des trades
- **Si l'EA ne trade pas** : vérifie que le spread est ≤ 1 (London/NY hours)
- **Ne fais pas confiance aux backtests à 100%** — commence avec `RiskPerTrade=0.5` et observe
