import os
import subprocess
import datetime
import whisperx
import torch
import yagmail
from dotenv import load_dotenv
from pathlib import Path
from pydub import AudioSegment

# Chargement variables d'environnement
load_dotenv()

# Paramètres
AUDIO_URL = "http://audio.bfmtv.com/bfmbusiness_128.mp3"
RECORD_SECONDS = 15  # Pour test rapide
OUTPUT_DIR = Path("run_cache")
OUTPUT_DIR.mkdir(exist_ok=True)
MODEL_SIZE = "small"  # rapide pour test
DIARIZATION = False   # on active après validation

EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_FROM = os.getenv("EMAIL_FROM")
