from asyncio.windows_events import CONNECT_PIPE_INIT_DELAY
import sqlite3
connection = sqlite3.connect ("combinations.db", timeout=10)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS ModifiedNumbers (
        first_dice INT,
        second_dice INT,
        third_dice INT,
        fourth_dice INT,
        fifth_dice INT,
        sixth_dice INT
    )""")
connection.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS DefaultNumbers (
        first_dice INT,
        second_dice INT,
        third_dice INT,
        fourth_dice INT,
        fifth_dice INT,
        sixth_dice INT
    )""")
connection.commit()
