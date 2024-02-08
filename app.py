from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello from my Dockerized Flask app!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
