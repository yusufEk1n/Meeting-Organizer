import sqlite3

"""
>>> program ilk çalıştırıldığında database.db dosyasında Meetings tablosunu oluşturur
>>> bazı seed verileri ekler
"""
def create_table():
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()

        cursor.execute('DROP TABLE IF EXISTS Meetings')
        
        cursor.execute('CREATE TABLE Meetings ( meeting_id INTEGER PRIMARY KEY, subject TEXT, date DATE, start_time TIME, end_time TIME, participants TEXT )')

        cursor.execute(' INSERT INTO Meetings (subject, date, start_time, end_time, participants) VALUES ("Meeting 1", "2021-01-01", "10:00", "11:00", "Person 1, Person 2, Person 3, Person 4, Person 5")')

        database.commit()

        cursor.close()
