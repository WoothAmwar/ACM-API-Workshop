from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Helper function to load data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(file_path, 'r') as f:
        return json.load(f)

@app.route('/api/names', methods=['GET'])
def get_names():
    data = load_data()
    names = [profile['profile_name'] for profile in data]
    return jsonify(names)

@app.route('/api/roles/<name>', methods=['GET'])
def get_role(name):
    data = load_data()
    for profile in data:
        if profile['profile_name'].lower() == name.lower():
            return jsonify({"name": profile['profile_name'], "role": profile['profile_image']})
    return jsonify({"error": "Name not found"}), 404

@app.route('/api/hobbies/<name>', methods=['GET'])
def get_hobbies(name):
    data = load_data()
    for profile in data:
        if profile['profile_name'].lower() == name.lower():
            return jsonify({"name": profile['profile_name'], "hobby": profile['profile_bio']})
    return jsonify({"error": "Name not found"}), 404

if __name__ == '__main__':
    print("Starting backend server on port 5000...")
    # Run the server on port 5000
    app.run(port=5000, debug=True)
