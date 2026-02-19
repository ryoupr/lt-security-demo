import sqlite3
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(filename='access.log', level=logging.INFO)

@app.route("/search")
def search_user():
    username = request.args.get("username")
    
    if not username:
        return jsonify({"error": "username parameter required"}), 400
    
    # セキュアなログ記録
    # 脆弱性ポイント: subprocess.run(f"echo 'searching {username}' >> access.log", shell=True)
    # 上記はコマンドインジェクション脆弱性 - ユーザー入力がシェルコマンドに直接渡される
    logging.info(f"Searching for user: {username}")
    
    # セキュアなDB検索
    # 脆弱性ポイント: f"SELECT * FROM users WHERE username = '{username}'"
    # 上記はSQLインジェクション脆弱性 - ユーザー入力がSQL文に直接埋め込まれる
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    results = cursor.fetchall()
    conn.close()
    
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=False)
