# battle.py

from flask import Blueprint, request, jsonify

battle_bp = Blueprint('battle', __name__)

@battle_bp.route('/start', methods=['POST'])
def start_battle():
    data = request.get_json()
    player1 = data.get('player1')
    player2 = data.get('player2')

    if not player1 or not player2:
        return jsonify({"error": "Both players must be provided"}), 400

    return jsonify({
        "message": f"Battle started between {player1} and {player2}",
        "status": "started"
    })
