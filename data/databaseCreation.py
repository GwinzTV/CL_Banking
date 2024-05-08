import sqlite3


#  creates or opens a file called bank.db
db = sqlite3.connect('../data/bank.db')

# cursor object used to execute SQL statements
cursor = db.cursor()

# create tables
cursor.execute('''
    CREATE TABLE users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password VARCHAR(40), name TEXT, surname, TEXT)
''')
cursor.execute('''
    CREATE TABLE account(account_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, username TEXT, balance INTEGER, FOREIGN KEY (user_id) REFERENCES users(user_id))
''')
db.commit()
