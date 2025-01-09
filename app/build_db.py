import sqlite3 

def setup_database():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute(
'''
CREATE TABLE IF NOT EXISTS users ()
''')
