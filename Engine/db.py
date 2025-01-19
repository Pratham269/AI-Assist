import sqlite3

con = sqlite3.connect("AI.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'Visual Studio Code', 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\OneNote.exe')"
#cursor.execute(query)
#con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'Youtube', 'https://www.youtube.com')"
cursor.execute(query)
con.commit()
