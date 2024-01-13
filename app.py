from flask import Flask, render_template, request, redirect, url_for, flash
import create_table as ct
import sqlite3
import os

app = Flask(__name__)

app.static_folder = os.path.abspath(path="templates/static/")

ct.create_table()

@app.route("/", methods=["GET"])
def index():
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute("SELECT * FROM Meetings")
        meetings = cursor.fetchall()
        
    return render_template("layouts/index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)