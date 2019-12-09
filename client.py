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

def searchByLast(input):
    search = "SELECT last_name, first_name FROM contacts WHERE last_name LIKE '" + input + "%'"
    c.execute(search)
    

def searchByFirst(input):
    search = "SELECT last_name, first_name FROM contacts WHERE first_name LIKE '" + input + "%'"
    c.execute(search)
    conn.commit()

def searchByFull(input_l, input_f):
    search = "SELECT last_name, first_name FROM contacts WHERE CONCAT(first_name, ' ', last_name) LIKE '%" + input_f + " " + input_l + "%'"
    c.execute(search)
    conn.commit()

def searchByCompany(input):
    search = "SELECT last_name, first_name, company_name FROM contacts WHERE company_name LIKE '" + input + "%'"
    c.execute(search)
    conn.commit()

def searchByAddr(input):
    search = "SELECT last_name, first_name, address FROM contacts WHERE address LIKE '" + input + "%'"
    c.execute(search)
    conn.commit()



