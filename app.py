from detoxify import Detoxify
import mariadb.connections
import pandas as pd
from flask import Flask, request, make_response, g
import mariadb
import os
import dotenv
from models.post import Post
import json

dotenv.load_dotenv()
model = Detoxify("multilingual")
toxicity_limit = 0.6
reset_mode = bool(os.environ.get("RESET_MODE"))
app = Flask(__name__)
config = {
    "host": os.environ.get("DB_HOST"),
    "port": int(os.environ.get("DB_PORT")),
    "database": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
}
print("config = %s" % config)
conn = None
try:
    conn = mariadb.connect(**config)
except Exception as e:
    print("Erreur lors de la connection à la base de donnée : %s" % e)

conn.autocommit = True
if reset_mode:
    conn.cursor().execute("DROP TABLE IF EXISTS Post")
conn.cursor().execute(
    """CREATE TABLE IF NOT EXISTS Post (
                            id BIGINT AUTO_INCREMENT PRIMARY KEY,
                            text TEXT NOT NULL,
                            datecreated DATETIME DEFAULT CURRENT_TIMESTAMP
)"""
)


@app.route("/api/post", methods=["GET"])
def get_post():
    cursor = conn.cursor()
    cursor.execute("SELECT id, text, datecreated FROM Post")
    rows = cursor.fetchall()
    print("-" * 1000)
    posts = []
    for row in rows:
        print(row)
        posts.append(Post(row[0], row[1], row[2]))
    return (json.dumps(posts, default=lambda p: p.__dict__), 200)


@app.route("/api/post", methods=["POST"])
def create_post():
    request_json = request.json
    if request_json is None:
        return make_response("", 404)
    else:
        text = request_json["text"]
        if text is None:
            return make_response("", 404)
        else:
            predict = model.predict([text])
            data_frame = pd.DataFrame(predict).round(5)
            is_toxic = bool(data_frame["toxicity"][0] >= toxicity_limit)
            if not is_toxic:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Post (text) VALUES (?)", (text,))
                cursor.execute("SELECT LAST_INSERT_ID()")
                id = cursor.fetchone()[0]
                cursor.execute("SELECT datecreated FROM Post WHERE id = ?", (id,))
                datecreated = cursor.fetchone()[0]
                cursor.close()
                post = Post(id, text, datecreated)
                return make_response(json.dumps(post.__dict__), 200)
            else:
                return make_response("", 400)


if __name__ == "__main__":
    print("-" * 100)
    print(os.environ.get("DB_HOST"))
    print("-" * 100)
    app.run(host=os.environ.get("ADDRESS"), port=os.environ.get("PORT"))
