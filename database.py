import sqlite3

def subscribe(user_id):
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT user_id FROM subscriptions WHERE user_id = '{user_id}'")
    print(type(user_id))
    if cursor.fetchone() is None:
        cursor.execute(f"INSERT INTO subscriptions VALUES (?, ?)",
                       (None, user_id))
        connection.commit()
        print("DONE")
    else:
        print("NOT DONE")

def add_tracking(track_id, status, country, date):
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT track_id FROM tracking WHERE track_id = '{track_id}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO tracking VALUES (?, ?, ?, ?, ?)",
                       (None, track_id, status, country, date))
        connection.commit()
        print("DONE")
    else:
        print("Data was added in table")

