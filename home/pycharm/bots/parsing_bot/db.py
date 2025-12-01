import sqlite3


def create_database():
    conn = sqlite3.connect('parced_works.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS parced_works
                (id INTEGER PRIMARY KEY AUTOINCREMENT, works TEXT)''')

    conn.commit()
    conn.close()


import sqlite3

def insert_into_db(parced_work: dict):
    conn = sqlite3.connect('parced_works.db')
    c = conn.cursor()

    # Check if the work data already exists in the database
    c.execute("SELECT works FROM parced_works")
    existing_works = [row[0] for row in c.fetchall()]

    if parced_work not in existing_works:
        c.execute("INSERT INTO parced_works (works) VALUES (?)", (str(parced_work),))
        conn.commit()
        print("Work data inserted successfully.")
    else:
        print("Work data already exists in the database.")

    conn.close()

