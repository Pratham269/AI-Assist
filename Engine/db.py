import csv
import sqlite3

con = sqlite3.connect("AI.db")
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'Word', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.exe')"
# cursor.execute(query)
# con.commit()


#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com')"
#cursor.execute(query)
#con.commit()

# delete_query = "DROP TABLE sys_command "
# cursor.execute(delete_query)
# con.commit()

# # Create a table with the desired columns
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# desired_columns_indices = [0,3]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

# #### 4. Insert Single contacts (Optional)

query = "INSERT INTO contacts VALUES (null,'Vaishnavi', '+917038344548',null)"
cursor.execute(query)
con.commit()

#delete a single row

# query = "DELETE FROM contacts WHERE id = 2;"
# cursor.execute(query)
# con.commit()

# #### 5. Search Contacts from database
# query = 'kunal'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])