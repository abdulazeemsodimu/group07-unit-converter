import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
HISTORY_FILE = DATA_DIR / "history.json"
DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_history():
if HISTORY_FILE.exists():
with open(HISTORY_FILE, "r", encoding="utf-8") as f:
return json.load(f)
return []

def save_history(history):
with open(HISTORY_FILE, "w", encoding="utf-8") as f:
json.dump(history, f, indent=2)