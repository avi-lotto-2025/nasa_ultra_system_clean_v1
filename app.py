import json
import os
from flask import Flask, jsonify
from engine_master import UltraEngine
from history_loader import HistoryLoader
from auto_heal import AutoHealEngine

app = Flask(__name__)

# -------------------------------------------------
# 1) טעינת היסטוריה + תיקון אוטומטי אם יש צורך
# -------------------------------------------------
HISTORY_PATH = "history_full.json"

print("[System] Loading history...")
loader = HistoryLoader(path=HISTORY_PATH)
history = loader.get_history()

# אם הקובץ ריק / תקול → להריץ AutoFix
if len(history) == 0:
    print("[AutoFix] No valid history found → running auto-repair...")
    fixer = AutoHealEngine()
    fixer.rebuild_history_file(HISTORY_PATH)
    loader = HistoryLoader(path=HISTORY_PATH)
    history = loader.get_history()

print(f"[System] Loaded {len(history)} valid historical draws.")

# -------------------------------------------------
# 2) יצירת מנוע NASA ULTRA
# -------------------------------------------------
engine = UltraEngine(history)

# -------------------------------------------------
# 3) API
# -------------------------------------------------
@app.route("/")
def home():
    return jsonify({"status": "NASA_ULTRA_SYSTEM_CLEAN_V1_RUNNING"})

@app.route("/forecast")
def forecast():
    result = engine.generate_forecast()
    return jsonify(result)

# -------------------------------------------------
# 4) MAIN
# -------------------------------------------------
if __name__ == "__main__":
    print("[System] Starting Flask server on port 8080...")
    app.run(host="0.0.0.0", port=8080)
