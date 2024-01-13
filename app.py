from flask import Flask, render_template, request, redirect, url_for, flash
import create_table as ct
import sqlite3
import os

app = Flask(__name__)

# templates/static/ dizinini statik dosyaların bulunduğu dizin olarak belirle
app.static_folder = os.path.abspath(path="templates/static/")

# Eğer database.db dosyası yoksa oluştur
if not os.path.exists("database.db"):
    ct.create_table()


"""
>>> sayfa ilk yüklendiğinde index() fonksiyonu çalışır
>>> database.db dosyasındaki Meetings tablosundaki tüm verileri çeker ve index.html sayfasına gönderir.
"""
@app.route("/", methods=["GET"])
def index():
    cursor = sqlite3.connect("database.db").cursor()
    cursor.execute("SELECT * FROM Meetings")
    meetings = cursor.fetchall()
        
    return render_template("layouts/index.html", meetings=meetings)


"""
>>> index.html sayfasında yeni toplantı formu gönderildiğinde insert() fonksiyonu çalışır
>>> formdan gelen verileri gerekli düzenlemeler yapıldıktan sonra database.db dosyasındaki Meetings tablosuna ekler
"""
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        subject = request.form['subject']
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        participants = request.form['participants']
        participants = participants.replace("\r\n", ",").strip(",")

        with sqlite3.connect("database.db") as database:
            cursor = database.cursor()
            cursor.execute('INSERT INTO Meetings (subject, date, start_time, end_time, participants) VALUES (?,?,?,?,?)', (subject, date, start_time, end_time, participants))
            database.commit()
            cursor.close()
    return redirect(url_for('index'))


"""
>>> index.html sayfasındaki toplantı listesindeki herhangi bir toplantı güncellenmek istendiğinde update() fonksiyonu çalışır
>>> gerekli düzenlemeleri yaptıktan sonra toplantı id'sine göre database.db dosyasındaki Meetings tablosundan ilgili toplantıyı günceller
"""
@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        subject = request.form['subject']
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        participants = request.form['participants']
        participants = participants.replace("\r\n", ",").strip(",")

        with sqlite3.connect("database.db") as database:
            cursor = database.cursor()
            cursor.execute('UPDATE Meetings SET subject = ?, date = ?, start_time = ?, end_time = ?, participants = ? WHERE meeting_id = ?', (subject, date, start_time, end_time, participants, id))
            database.commit()
            cursor.close()
            return redirect(url_for('index'))

"""
>>> index.html sayfasındaki toplantı listesindeki herhangi bir toplantı silinmek istendiğinde delete() fonksiyonu çalışır
>>> toplantı id'si ile database.db dosyasındaki Meetings tablosundan ilgili toplantıyı siler
"""
@app.route('/delete/<int:id>', methods = ['GET'])
def delete(id):
    with sqlite3.connect("database.db") as database:
        cursor = database.cursor()
        cursor.execute('DELETE FROM Meetings WHERE meeting_id = ?', (id,))
        database.commit()
        cursor.close()
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)