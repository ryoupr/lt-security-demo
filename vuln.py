import subprocess
import sqlite3

# CWE-798: ハードコード秘密情報
API_KEY = "AKIAIOSFODNN7EXAMPLE"
db_password = "admin123"


# CWE-78: コマンドインジェクション
def ping_host(hostname):
    subprocess.Popen(f"ping {hostname}", shell=True)


# CWE-89: SQLインジェクション
def get_user(user_id):
    conn = sqlite3.connect("app.db")
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return conn.execute(query).fetchall()
