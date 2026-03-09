from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)

current_sound = ""

@app.route("/")
def overlay():
    return send_from_directory(".", "index.html")

@app.route("/sound")
def sound():
    global current_sound
    s = current_sound
    current_sound = ""
    return s

@app.route("/redeem")
def redeem():
    global current_sound
    current_sound = request.args.get("sound","")
    return "ok"

@app.route("/<path:file>")
def serve_file(file):
    return send_from_directory(".", file)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
