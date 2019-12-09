import sqlite3

conn = sqlite3.connect('contacts.db')
c = conn.cursor()

def createTable():
    createContactTable = """CREATE TABLE contacts (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                company_name TEXT,
                address TEXT,
                email TEXT,
                phone TEXT
                )"""
    c.execute(createContactTable)
    conn.commit()

def createContact(task):
    sql = ''' INSERT INTO contacts(id, first_name, last_name, company_name, address, email, phone)
              VALUES(?,?,?,?,?,?,?) '''
    c.execute(sql, task)
    conn.commit()
