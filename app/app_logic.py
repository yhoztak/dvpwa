from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Insecure database connection
DATABASE = "vulnerable.db"

# Create a vulnerable SQLite database
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
    conn.commit()
    conn.close()


# SQL Injection Vulnerability
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Vulnerable query: Directly inserting user input into SQL
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    result = c.execute(query).fetchone()
    conn.close()
    
    if result:
        return jsonify({"message": f"Welcome, {username}!"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# Cross-Site Scripting (XSS) Vulnerability
@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")
    return f"<h1>Welcome, {name}!</h1>"  # Directly rendering user input into HTML


# Command Injection Vulnerability
@app.route("/ping", methods=["GET"])
def ping():
    ip = request.args.get("ip")
    if not ip:
        return "IP address is required", 400

    # Vulnerable to command injection
    stream = os.popen(f"ping -c 1 {ip}")
    output = stream.read()
    return f"<pre>{output}</pre>"


# Insecure File Upload Vulnerability
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if file:
        file.save(f"./uploads/{file.filename}")  # No validation on file type or path
        return jsonify({"message": "File uploaded!"})
    return jsonify({"message": "No file uploaded"}), 400


if __name__ == "__main__":
    app.run(debug=True)
