import sqlite3
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/search")
def search_user():
    username = request.args.get("username")
    subprocess.run(f"echo 'searching {username}' >> access.log", shell=True)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    results = cursor.fetchall()
    conn.close()
    return jsonify(results)
