import json
from pathlib import Path

# Define project root directory (two levels up from this file)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define data directory and history file path
DATA_DIR = PROJECT_ROOT / "data"
HISTORY_FILE = DATA_DIR / "history.json"

# Ensure the data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_history():
    """
    Load conversion history from the history.json file.

    Returns:
        list: A list of conversion records, where each record is a dictionary
              containing details of a past conversion.
              Returns an empty list if no history file exists.
    """
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_history(history):
    """
    Save the given conversion history to the history.json file.

    Args:
        history (list): A list of conversion records to be saved.
                        Each record should be a dictionary.
    """
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

def add_record(value, from_unit, to_unit, result, category):
    """
    Add a new conversion record to the history.

    Args:
        value (float): The input value that was converted.
        from_unit (str): The unit of the input value.
        to_unit (str): The target unit of conversion.
        result (float): The result of the conversion.
        category (str): The conversion category (e.g., "length", "mass", "temperature").

    Returns:
        dict: The newly added record.
    """
    record = {
        "value": value,
        "from": from_unit,
        "to": to_unit,
        "result": result,
        "category": category
    }
    history = load_history()
    history.insert(0, record)
    save_history(history)
    return record

def clear_history():
     """
    Clear all conversion history by overwriting history.json with an empty list.
    """
    save_history([])
