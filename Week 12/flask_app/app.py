from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    return jsonify(user) if user else ('', 404)

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    if not new_user or 'name' not in new_user:
        return jsonify({'error': 'Invalid user data'}), 400

    # Assign a unique ID
    new_user['id'] = max(user['id'] for user in users) + 1 if users else 1
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)
