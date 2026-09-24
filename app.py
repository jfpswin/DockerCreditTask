import os
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

# set to default 5000
PORT = int(os.environ.get("PORT", 5000))


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from my credit task Flask app!",
        "hostname": os.environ.get("HOSTNAME", "unknown"),
        "time": datetime.now().isoformat() + "Z"
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # 0.0.0.0 so app is reachable outside container
    app.run(host="0.0.0.0", port=PORT)
