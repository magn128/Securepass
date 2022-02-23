import sqlite3

# Connect to database or create new
conn = sqlite3.connect('test1.db')
# Cursor to execute commands
c = conn.cursor()


def createcategoryTable(c, db_name, firstRow):
     #c.execute("CREATE TABLE :db_name(:firstRow text)", {'db_name': db_name, 'firstRow': firstRow})
     c.execute(f"CREATE TABLE :{db_name}(:{firstRow} text)")

def category(name):
    c.execute("INSERT INTO login VALUES (:name)", {"name": name})
# Create new table
def createloginTable(c, db_name, firstRow, secondRow):
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