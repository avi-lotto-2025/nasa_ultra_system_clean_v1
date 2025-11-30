import json
from official_fetch_engine import OfficialFetcher

class HistoryLoader:

    def load(self):
        try:
            with open("history_full.json", "r", encoding="utf-8") as f:
                history = json.load(f)
        except:
            history = []

        latest = OfficialFetcher().fetch_latest()

        if latest:
            if history and history[-1]["main"] == latest["main"]:
                return history
            history.append(latest)

            with open("history_full.json", "w", encoding="utf-8") as f:
                json.dump(history, f, ensure_ascii=False, indent=2)

        return history
