import json
import os

class HistoryLoader:
    def __init__(self, path="history_full.json"):
        self.path = path
        self.history = self.load_history()

    def load_history(self):
        """
        טוען את היסטוריית ההגרלות בצורה בטוחה לחלוטין.
        אם הקובץ חסר / ריק / פגום – המערכת לא נופלת.
        """
        # 1) האם הקובץ בכלל קיים?
        if not os.path.exists(self.path):
            print(f"[HistoryLoader] WARNING: file {self.path} not found. Using empty history.")
            return []

        # 2) נסיון לקרוא בצורה בטוחה
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # 3) בדיקה שהתוכן הוא רשימה תקינה
            if not isinstance(data, list):
                print("[HistoryLoader] WARNING: history file is not a list. Using empty history.")
                return []

            # 4) וידוא שכל איבר ברשימה תקין (רשימת מספרים)
            clean_data = []
            for item in data:
                if isinstance(item, list) and all(isinstance(n, int) for n in item):
                    clean_data.append(item)

            if len(clean_data) == 0:
                print("[HistoryLoader] WARNING: history file contains no valid entries.")
                return []

            return clean_data

        except Exception as e:
            # 5) במקרה של קריסת JSON / תקלה בקריאה
            print(f"[HistoryLoader] ERROR reading history file: {e}. Using empty history.")
            return []

    def get_history(self):
        """ מחזיר את ההיסטוריה, תמיד בצורה בטוחה """
        return self.history
