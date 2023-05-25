import mysql.connector

db_connection = mysql.connector.connect(
host="db4free.net",
user="nazmul",
passwd="123456789",
database="nazmul"
)

db_cursor = db_connection.cursor()
#Here creating database table as student'
db_cursor.execute("CREATE TABLE student (School_id INT, School_name VARCHAR(255))")
#Get database table'
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)