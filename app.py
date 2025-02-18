from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-password")
def generate_password():
    length = 12  # You can make this dynamic
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return jsonify(password=password)

if __name__ == "__main__":
    app.run(debug=True)
