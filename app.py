from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/api/info")
def api_info():
    return jsonify(
        application="Velzz FTMS",
        course="Cloud Computing",
        code="PTI 2802",
        deployment="AWS EC2 Ubuntu 24.04",
        status="ok"
    ), 200
