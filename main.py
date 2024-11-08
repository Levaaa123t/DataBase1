import sqlite3 
con = sqlite3.connect("YouTube.db") # соединение с базой данных, если бд нет, то файл создастся

cur = con.cursor()
#cur.execute("CREATE TABLE videos(id, title, year, author, link)")
cur.execute(""" 
            DELETE FROM videos WHERE id = 3
            """)
con.commit()

for row in cur.execute("""SELECT * FROM videos """):
    print(row)
con.close()