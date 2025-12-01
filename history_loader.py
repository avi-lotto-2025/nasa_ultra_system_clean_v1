import json
import os

class HistoryLoader:
    def __init__(self, path="history_full.json"):
        self.path = path

    def load(self):
        """
        טוען את ההיסטוריה מהקובץ בצורה בטוחה.
        """
        if not os.path.exists(self.path):
            print(f"[HistoryLoader] WARNING: history file {self.path} not found. Using empty history.")
            return []

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, list):
                print("[HistoryLoader] WARNING: history file is not list. Using empty history.")
                return []

            clean = []
            for item in data:
                if isinstance(item, list) and all(isinstance(n, int) for n in item):
                    clean.append(item)

            if len(clean) == 0:
                print("[HistoryLoader] WARNING: history file contains no valid entries.")
                return []

            return clean

        except Exception as e:
            print(f"[HistoryLoader] ERROR reading history file: {e}")
            return []

