import sqlite3
connect = sqlite3.connect("c://sqlite//hcl.db")
cur = connect.cursor()  # cursor object
# conn.execute('''CREATE TABLE Log(ID INT PRIMARY KEY    NOT NULL);''')
# print("Table created")
# conn.execute('''Insert into filelog values(10);''')

sql = """insert into filelog values(?, ?);"""
data = (100, 'C:/jose/demo.html')
cur.execute(sql,data)
connect.commit()
cur.execute("select * from filelog where id=100");
rows=cur.fetchall()
for r in rows:
    print(r)