#!/usr/bin/python3
"""Module for basic serialization using JSON."""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/user/<username>')
def user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    '''Handles POST requests to add new users'''
    user_data = request.get_json()
    if not user_data or 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400
    username = user_data['username']
    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__": 
    app.run()
