from flask import Flask
import create_table as ct
import sqlite3

app = Flask(__name__)

#ilk olarak database.db dosyasını oluşturuyoruz
ct.create_table()

@app.route("/", methods=["GET"])
def index():
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute("SELECT * FROM Meetings")
        meetings = cursor.fetchall()
        return str(meetings)
        


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)