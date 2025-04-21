import sqlite3

def create_database():
    conn = sqlite3.connect('trainer.db')
    conn.execute("PRAGMA foreign_keys = ON")
    
    with open('create_tables.sql', 'r') as f:
        conn.executescript(f.read())
    
    conn.commit()
    print("Database created successfully!")
    conn.close()

create_database()