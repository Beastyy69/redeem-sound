from flask import Flask, send_file, request

app = Flask(__name__)

current_sound=""

@app.route("/")
def overlay():
    return send_file("index.html")

@app.route("/sound")
def get_sound():
    return current_sound

@app.route("/redeem")
def redeem():
    global current_sound
    current_sound = request.args.get("sound","")
    return "ok"

if __name__ == "__main__":
    app.run()