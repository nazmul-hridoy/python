'''
Now browse any table, as for example location_taw and see the existing data.
This program will fetch all data from this table.
'''

import mysql.connector

'''
Create Connection
'''
connection = mysql.connector.connect(host='db4free.net',
                                         database='nazmul',
                                         user='nazmul',
                                         password= '123456789',
                                         autocommit = True)
cursor = connection.cursor()

'''
Fetch data from database and print line by line
'''

sql_select_Query = "select * from `table_school`"
cursor.execute(sql_select_Query)
results = cursor.fetchall()
for index, value in enumerate(results):
    print(value)
    


