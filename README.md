# BFM Transcriber — Version Colab exportée

Script exporté depuis Google Colab (tests OK).
Ce dépôt contient :
- le script Python exporté de Colab (toutes les cellules)
- `requirements.txt` (dépendances validées)

## Structure
- `bfm_transcriber.py` (ou `transcriber_raw.py`) : code exporté
- `requirements.txt` : versions alignées avec Colab (CPU)
- `README.md` : ce fichier

## (Pour plus tard) Installation sur serveur
Quand on passera au serveur (Ionos VPS) :
```bash
sudo apt-get update
sudo apt-get install -y ffmpeg git python3-venv python3-pip
git clone <URL_DU_REPO>.git
cd <NOM_DU_REPO>
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
