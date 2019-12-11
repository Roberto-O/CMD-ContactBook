import sqlite3

conn = sqlite3.connect('contacts.db')
c = conn.cursor()

def createTable():
    createContactTable = """CREATE TABLE contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                company_name TEXT,
                address TEXT,
                email TEXT,
                phone TEXT
                )"""
    c.execute(createContactTable)
    conn.commit()

def showContacts():
    sql = "SELECT * FROM contacts"
    c.execute(sql)
    conn.commit()
    rows = c.fetchall()
    return rows


def searchByLast(input):
    search = "SELECT id, last_name, first_name FROM contacts WHERE last_name LIKE '" + input + "%'"
    c.execute(search)
    conn.commit()
    rows = c.fetchall()
    return rows


def selectById(task):
    sql = "SELECT * FROM contacts WHERE id = " + task
    c.execute(sql)
    conn.commit()
    row = c.fetchone()
    return row


def searchByFirst(input): #THIS IS THE CORRECT FORMAT
    search = "SELECT id, last_name, first_name FROM contacts WHERE first_name LIKE '" + input + "%'"
    c.execute(search)
    conn.commit()
    rows = c.fetchall()
    return rows


def searchByFull(input_l, input_f):
    search = "SELECT id, last_name, first_name FROM contacts WHERE first_name || ' ' || last_name LIKE '%" + input_f + " " + input_l + "%'"
    c.execute(search)
    conn.commit()
    rows = c.fetchall()
    return rows


def searchByCompany(input):
    search = "SELECT id, last_name, first_name, company_name FROM contacts WHERE company_name LIKE '" + input + "%'"
    c.execute(search)
    conn.commit()
    rows = c.fetchall()
    return rows


def searchByEmail(input):
    search = "SELECT id, last_name, first_name, company_name FROM contacts WHERE email LIKE '" + input + "%'"
    c.execute(search)
    conn.commit()
    rows = c.fetchall()
    return rows


def searchByAddr(input):
    search = "SELECT id, last_name, first_name, address FROM contacts WHERE address LIKE '" + input + "%'"
    c.execute(search)
    conn.commit()
    rows = c.fetchall()
    return rows


def createContact(task):
    sql = ''' INSERT INTO contacts(first_name, last_name, company_name, address, email, phone)
              VALUES(?,?,?,?,?,?) '''
    c.execute(sql, task)
    conn.commit()

def updateLastName(task):
    sql = ''' UPDATE contacts
             SET last_name = ?
             WHERE id = ? '''
    c.execute(sql, task)
    conn.commit()

def updateFirstName(task):
    sql = ''' UPDATE contacts
             SET first_name = ?
             WHERE id = ? '''
    c.execute(sql, task)
    conn.commit()

def updateCompany(task):
    sql = ''' UPDATE contacts
             SET company_name = ?
             WHERE id = ? '''
    c.execute(sql, task)
    conn.commit()

def updateAddr(task):
    sql = ''' UPDATE contacts
             SET address = ?
             WHERE id = ? '''
    c.execute(sql, task)
    conn.commit()

def updateNum(task):
    sql = ''' UPDATE contacts
             SET phone = ?
             WHERE id = ? '''
    c.execute(sql, task)
    conn.commit()

def updateEmail(task):
    sql = ''' UPDATE contacts
             SET email = ?
             WHERE id = ? '''
    c.execute(sql, task)
    conn.commit()

def removeContact(task):
    sql = 'DELETE FROM contacts WHERE id=?'
    c.execute(sql, (task,))
    conn.commit()
