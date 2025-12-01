import sqlite3

def users():
    conn = sqlite3.connect('users.db')
    conn.execute("SELECT * FROM user")
    rows = conn.cursor().fetchall()

    return rows

print(users())