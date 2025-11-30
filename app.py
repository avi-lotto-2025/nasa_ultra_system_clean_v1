from flask import Flask, jsonify
from engine_master import EngineMaster

app = Flask(__name__)
engine = EngineMaster()

@app.route("/forecast")
def forecast():
    return jsonify(engine.generate_full())

@app.route("/health")
def health():
    return jsonify(engine.health())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
