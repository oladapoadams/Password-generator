from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

# Function to generate a secure password
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

# Route to serve the frontend
@app.route('/')
def home():
    return render_template('index.html')

# API Route to generate password
@app.route('/generate-password', methods=['GET'])
def get_password():
    password = generate_password()
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
