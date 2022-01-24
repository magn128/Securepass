import sqlite3

# Connect to database or create new
conn = sqlite3.connect('test.db')
# Cursor to execute commands
c = conn.cursor()

# Create new table
def createTable(db_name, firstRow, secondRow):
    c.execute("""CREATE TABLE :db_name(
        :firstRow text,
        :secondRow text
        )""", {"db_name": db_name, "firstRow": firstRow, "secondRow": secondRow})
# Insert values into table
def insert(name, password):
    c.execute("INSERT INTO login VALUES (:name, :password)", {"name": name, "password": password})

# Commiting changes
conn.commit()
conn.close()
