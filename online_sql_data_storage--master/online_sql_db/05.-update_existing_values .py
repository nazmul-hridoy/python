'''
This code will modify the value of an existing entry in the database
'''
import mysql.connector

'''
Create Connection
'''
connection = mysql.connector.connect(host='db4free.net',
                                         database='nazmul',
                                         user='nazmul',
                                         password='123456789',
                                         autocommit = True)
cursor = connection.cursor()

'''
In the table_school, at School_id = 14, Total_bunch = 2.
We want to modify Total_brunch = 4 where School_id = 14.
'''
sql_update_query = """Update table_school set Total_brunch = '4' where School_id = 14"""
cursor.execute(sql_update_query)


'''
Here, In the table_school, at School_id = 14.
We want to delete where School_id = 14
'''
query = "DELETE FROM table_school WHERE `table_school`.School_id = 14"
cursor.execute(query)

