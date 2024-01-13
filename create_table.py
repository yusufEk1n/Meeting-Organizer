import sqlite3

def create_table():
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()

        cursor.execute('DROP TABLE IF EXISTS Meetings')
        
        cursor.execute('CREATE TABLE Meetings ( meeting_id INTEGER PRIMARY KEY, subject TEXT, date DATE, start_time TIME, end_time TIME, participants TEXT )')

        cursor.execute(' INSERT INTO Meetings (subject, date, start_time, end_time, participants) VALUES ("Meeting 1", "2021-01-01", "10:00", "11:00", "Person 1, Person 2")')

        database.commit()
