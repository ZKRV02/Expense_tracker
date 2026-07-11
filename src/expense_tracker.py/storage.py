import json
from pathlib import Path

HOME_DIR = Path.home()
DATA_FILE = HOME_DIR / ".expense_tracker_data.json"

def load_expenses():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            expenses = json.load(file)
            if not isinstance(expenses, list): 
                return []
            return expenses
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)
