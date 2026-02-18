from flask import Flask, request
import subprocess
import sqlite3

app = Flask(__name__)

# CWE-798: ハードコード秘密情報
API_KEY = "AKIAIOSFODNN7EXAMPLE"
db_password = "admin123"


# CWE-78: コマンドインジェクション
@app.route("/ping")
def ping():
    hostname = request.args.get("host")
    result = subprocess.Popen(f"ping {hostname}", shell=True)
    return str(result)


# CWE-89: SQLインジェクション
@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("app.db")
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return str(conn.execute(query).fetchall())


if __name__ == "__main__":
    app.run()
# demo trigger
