from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Sample database to store user credentials
users = {
    'your_username': 'your_password'
}

# Sample database to store issued tokens
tokens = {}

# Endpoint for generating a Bearer Token
@app.route('/get_token', methods=['POST'])
def get_token():
    # Get username and password from the request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the username and password match
    if users.get(username) == password:
        # Generate a unique token
        token = str(uuid.uuid4())

        # Store the token and associated user data in the database
        tokens[token] = username

        # Return the token as a JSON response
        return jsonify({'token': token})

    # Return an error message if authentication fails
    return jsonify({'error': 'Authentication failed'}), 401

# Protected endpoint that requires a valid Bearer Token
@app.route('/protected', methods=['GET'])
def protected():
    # Get the Bearer Token from the request header
    token = request.headers.get('Authorization')

    # Check if the token is valid
    if token and token.startswith('Bearer '):
        token = token.split(' ')[1]
        if token in tokens:
            # Get the associated data for the token
            user_data = tokens[token]

            # Return a protected resource for the authenticated user
            return jsonify({'message': f'Hello, {user_data}! This is a protected resource.'})

    # Return an error message if the token is invalid
    return jsonify({'error': 'Invalid token'}), 401


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=5020)