from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_FILE = '../data/anime_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/anime', methods=['GET'])
def get_anime():
    data = load_data()
    return jsonify(data)

@app.route('/anime', methods=['POST'])
def add_anime():
    new_anime = request.json
    data = load_data()
    data.append(new_anime)
    save_data(data)
    return jsonify({"message": "Anime berhasil ditambahkan"}), 201

@app.route('/anime/<int:index>', methods=['PUT'])
def update_anime(index):
    data = load_data()
    if 0 <= index < len(data):
        updated = request.json
        data[index].update(updated)
        save_data(data)
        return jsonify({"message": "Anime berhasil diperbarui"})
    return jsonify({"error": "Anime tidak ditemukan"}), 404

@app.route('/anime/<int:index>/character', methods=['POST'])
def add_character(index):
    data = load_data()
    if 0 <= index < len(data):
        new_char = request.json
        data[index].setdefault("characters", []).append(new_char)
        save_data(data)
        return jsonify({"message": "Karakter berhasil ditambahkan"})
    return jsonify({"error": "Anime tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run(debug=True)