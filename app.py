from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# definir constante url
character_url = 'https://rickandmortyapi.com/api/character/'

@app.route('/character', methods=['POST'])
def get_character():

    if not request.is_json or not request.get_json().get('character_id'):
        return jsonify({"error": "Character ID is required"}), 400

    try:
        character_id = int(request.get_json().get('character_id'))
    except ValueError:
        return jsonify({"error": "Character is not a number"}), 400

    response = requests.get(f'{character_url}{character_id}')
        
    if response.status_code != 200:
        return jsonify({"error": "Character not found"}), 404
    else:
        character_data = response.json()
        return jsonify({
            "name": character_data['name'],
            "status": character_data['status']
        })
    
if __name__ == '__main__':
    app.run(debug=True)
