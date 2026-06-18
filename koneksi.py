import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="healthcare_db"
)

cursor = conn.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)

conn.close()