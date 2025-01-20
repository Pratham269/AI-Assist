import sqlite3

con = sqlite3.connect("AI.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'Excel', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.exe')"
#cursor.execute(query)
#con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com')"
#cursor.execute(query)
#con.commit()

#delete_query = "DELETE FROM sys_command WHERE id = ?"
#row_id = 4
#cursor.execute(delete_query, (row_id,))
#con.commit()