import sqlite3

def read_users():
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        return sorted(rows)
    finally:
        cursor.close()
        conn.close()

def find_users_by_fio():
    name = str(input('Enter victims name (Name): '))
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        # Use parameterized query to prevent SQL injection
        cursor.execute('SELECT * FROM user WHERE Name = ?', (name,))
        rows = cursor.fetchall()
        return sorted(rows)
    finally:
        cursor.close()
        conn.close()

print(read_users())