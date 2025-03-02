from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simulated database
users = []

@app.route('/')
def home():
    return "Unified AI Platform Backend is Running!"

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    
    if not username or not email:
        return jsonify({"error": "Missing username or email"}), 400
    
    user = {"username": username, "email": email}
    users.append(user)
    return jsonify({"message": "User signed up successfully!", "user": user})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
