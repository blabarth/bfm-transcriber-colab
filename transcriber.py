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

def record_audio():
    """Enregistre le flux audio pendant RECORD_SECONDS secondes."""
    output_mp3 = OUTPUT_DIR / "record.mp3"
    cmd = [
        "ffmpeg", "-y", "-i", AUDIO_URL,
        "-t", str(RECORD_SECONDS),
        "-acodec", "mp3",
        str(output_mp3)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_mp3
def transcribe_audio(audio_path):
    """Transcrit l'audio avec WhisperX."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisperx.load_model(MODEL_SIZE, device)
    audio = whisperx.load_audio(str(audio_path))
    result = model.transcribe(audio)
    return result.get("text", "")
def send_email(subject: str, body: str):
    """Envoie la transcription par email via Gmail (mot de passe d'application)."""
    email_from = os.getenv("EMAIL_FROM")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_to = os.getenv("EMAIL_TO")

    if not (email_from and email_password and email_to):
        print("[WARN] Variables EMAIL_FROM / EMAIL_PASSWORD / EMAIL_TO manquantes, email non envoyé.")
        return

    try:
        yag = yagmail.SMTP(email_from, email_password)
        yag.send(to=email_to, subject=subject, contents=body)
        print("[OK] Email envoyé à", email_to)
    except Exception as e:
        print("[ERR] Envoi email a échoué:", e)
if __name__ == "__main__":
    print("[INFO] Démarrage du script...")
    audio_path = record_audio()
    print("[INFO] Enregistrement terminé :", audio_path)

    transcription = transcribe_audio(audio_path)
    print("[INFO] Transcription terminée.")

    send_email("Transcription BFM", transcription)
    print("[INFO] Script terminé.")
