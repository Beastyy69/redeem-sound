from flask import Flask, send_file, request
import os

app = Flask(__name__)

current_sound = ""

@app.route("/")
def overlay():
    return send_file("index.html")

@app.route("/sound")
def sound():
    global current_sound
    sound = current_sound
    current_sound = ""
    return sound

@app.route("/redeem")
def redeem():
    global current_sound
    current_sound = request.args.get("sound","")
    return "ok"

@app.route("/<filename>")
def get_file(filename):
    return send_file(filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
