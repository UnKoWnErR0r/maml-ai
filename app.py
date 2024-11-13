from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Meta-Learning API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
