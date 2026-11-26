from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return make_response("Welcome to Flask Application! Version1", 200)

@app.route("/status")
def status():
    return make_response(jsonify({
        "status": "UP",
        "message": "Application is running"
    }), 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
