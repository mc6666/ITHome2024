import sqlite3

con = sqlite3.connect("calendar.db")
cur = con.cursor()
# cur.execute("CREATE TABLE calendar(id, text, start, end)")
data = [
    (None, "Event 1", "2024-10-10T10:30:00", "2024-10-10T12:30:00"),
    (None, "Event 2", "2024-10-11T12:30:00", "2024-10-11T14:30:00"),
    (None, "Event 3", "2024-10-12T10:00:00", "2024-10-12T17:00:00"),
]
cur.executemany("INSERT INTO calendar VALUES(?, ?, ?, ?)", data)
con.commit() 
con.close()