import os
import json
from flask import Flask, jsonify

# ======================================================
#   AUTOFIX ENGINE – תיקון אוטומטי מלא לפני עליית השרת
# ======================================================

class AutoFixEngine:

    REQUIRED_FILES = {
        "history_loader.py": """
import json
import os

class HistoryLoader:
    def __init__(self, path="history_full.json"):
        self.path = path
        self.history = self.load()

    def load(self):
        if not os.path.exists(self.path):
            print(f"[HistoryLoader] WARNING: history file {self.path} not found. Using empty history.")
            return []

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, list):
                print("[HistoryLoader] WARNING: history is not a list – using empty.")
                return []

            clean = []
            for item in data:
                if isinstance(item, list) and all(isinstance(n, int) for n in item):
                    clean.append(item)

            if len(clean) == 0:
                print("[HistoryLoader] WARNING: no valid entries in history.")
                return []

            return clean

        except Exception as e:
            print(f"[HistoryLoader] ERROR reading file: {e}")
            return []

    def get_history(self):
        return self.history
""",

        "history_full.json": "[]"
    }

    REQUIRED_METHODS = {
        "HistoryLoader": ["load", "get_history"]
    }

    def __init__(self, base_path="/app"):
        self.base = base_path

    # -------------------------------
    # יצירת קבצים חסרים
    # -------------------------------
    def fix_missing_files(self):
        for filename, content in self.REQUIRED_FILES.items():
            full = os.path.join(self.base, filename)
            if not os.path.exists(full):
                print(f"[AutoFix] FILE MISSING → {filename} → Creating default.")
                with open(full, "w", encoding="utf-8") as f:
                    f.write(content)

    # -------------------------------
    # תיקון מחלקות / פונקציות חסרות
    # -------------------------------
    def fix_loader_integrity(self):
        file_path = os.path.join(self.base, "history_loader.py")
        if not os.path.exists(file_path):
            return

        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        # אם חסרה המחלקה או פונקציה → משחזרים את הקובץ המלא
        if "class HistoryLoader" not in code:
            print("[AutoFix] Missing class HistoryLoader → Rebuilding file.")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.REQUIRED_FILES["history_loader.py"])
            return

        for method in self.REQUIRED_METHODS["HistoryLoader"]:
            if f"def {method}" not in code:
                print(f"[AutoFix] Missing method {method} → Rebuilding file.")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(self.REQUIRED_FILES["history_loader.py"])
                return

    # -------------------------------
    # הרצת כל התיקונים
    # -------------------------------
    def run(self):
        print("[AutoFix] Running automatic repair...")
        self.fix_missing_files()
        self.fix_loader_integrity()
        print("[AutoFix] Completed.")


# ======================================================
#   הפעלת התיקון לפני טעינת מנוע החיזוי
# ======================================================

AutoFixEngine().run()

# ======================================================
#   טעינת מנוע החיזוי לאחר תיקון הקבצים
# ======================================================

from history_loader import HistoryLoader

class EngineMaster:
    def __init__(self):
        self.history = HistoryLoader().get_history()

    def generate_forecast(self):
        import random
        return {
            "main": sorted(random.sample(range(1, 38), 6)),
            "extra": random.randint(1, 7)
        }

# ======================================================
#   FLASK API
# ======================================================

app = Flask(__name__)
engine = EngineMaster()

@app.route("/forecast")
def forecast():
    result = engine.generate_forecast()
    return jsonify(result)

@app.route("/")
def home():
    return jsonify({"status": "NASA ULTRA ONLINE"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
