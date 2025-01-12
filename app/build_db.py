import sqlite3 

def setup_database():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY UNIQUE,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_1 TEXT ,
            user_2 TEXT,
            user_3 TEXT,
            user_4 TEXT,
            user_5 TEXT,
            user_6 TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS moves (
            game_id INTEGER,
            user_id INTEGER,
            type TEXT NOT NULL,
            hand TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == '__main__':
    setup_database()
