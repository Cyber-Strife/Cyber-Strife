# server.py

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "online",
        "message": "Cyber Strife API is up and running!"
    })

@app.route('/api/battle', methods=['POST'])
def battle():
    # Sample battle logic
    return jsonify({
        "status": "success",
        "message": "Battle initiated successfully"
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
