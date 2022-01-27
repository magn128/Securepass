import sqlite3

def db_connection(db_name, db, createT, firstRow, secondRow, name, password):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    createTable(createT, db_name, firstRow, secondRow)
    insert(name, password)

# Create new table
def createTable(createT, db_name, firstRow, secondRow):
    if createT:
        c.execute("""CREATE TABLE :db_name(
            :firstRow text,
            :secondRow text
            )""", {"db_name": db_name, "firstRow": firstRow, "secondRow": secondRow})
    else:
        pass

# Insert values into table
def insert(name, password):
    c.execute("INSERT INTO login VALUES (:name, :password)", {"name": name, "password": password})

# Commiting changes
conn.commit()
conn.close()
