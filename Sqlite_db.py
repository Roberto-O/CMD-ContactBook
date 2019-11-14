import sqlite3

conn = sqlite3.connect('contacts.db')

c = conn.cursor()

c.execute("CREATE TABLE  users(
                id INTEGER PRIMARY KEY,
                login TEXT,
                password TEXT,
                name TEXT,
                )")
conn.commit()

c.execute("CREATE TABLE contact (
                id INTEGER PRIMARY KEY,
                user_id INTEGER
                name TEXT,
                email TEXT,
                phone INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
                )")
conn.commit()
