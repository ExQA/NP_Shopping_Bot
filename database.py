import mysql.connector
from loguru import logger

DB = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='qazqaz123123',
    port='3306',
    database='np_shoping'
)

logger.add(
    "debug.json", format="{format} {level} {message}",
    level="DEBUG", serialize=True
)

@logger.catch
def subscribe(user_id):
    cursor = DB.cursor()

    cursor.execute(f"SELECT user_id FROM subscriptions WHERE user_id = '{user_id}'")
    print(type(user_id))
    if cursor.fetchone() is None:
        cursor.execute(f"INSERT INTO subscriptions VALUES (%s, %s)",
                       (None, user_id))
        DB.commit()
    else:
        print("NOT DONE")

@logger.catch
def add_tracking(track_id, status, country, date):
    cursor = DB.cursor()

    cursor.execute(f"SELECT track_id FROM np_shoping.tracking WHERE track_id = '{track_id}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO np_shoping.tracking VALUES (%s, %s, %s, %s, %s)",
                       (None, track_id, status, country, date))
        DB.commit()
    else:
        print("Data was added in table")
