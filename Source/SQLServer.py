
import MySQLdb

dbconnect = MySQLdb.connect("localhost", "sanjayraokadali", "23March_an", "UserDB")

cursor = dbconnect.cursor()
cursor.execute("SELECT * from UserDB.test;")

data = cursor.fetchall()

print(data)

cursor.execute(f"""

          INSERT INTO userdb.test values
          ('Bob', 12);
""")

cursor.execute("commit;")

cursor.execute("SELECT * from UserDB.test;")

data = cursor.fetchall()

print(data)



dbconnect.close()