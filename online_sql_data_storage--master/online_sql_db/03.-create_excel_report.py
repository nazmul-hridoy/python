'''
Here we will generate an excel file using the fetched data from database.
This code will be a continuation of the previous one.
'''

import mysql.connector
import pandas as pd

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
Fetch data from database and print line by line
'''

sql_select_Query = "select * from `table_school`"
cursor.execute(sql_select_Query)
results = cursor.fetchall()
for index, value in enumerate(results):
    print(value)
    
'''
Create excel report
'''
data_to_write = []
for index, value in enumerate(results):
    data_to_write.append(value)

df_data_to_write = pd.DataFrame(data_to_write, columns =['School_id', 'School_name', 'Main_brunch', 'Total_class', 'Total_area', 'Total_student'])
excel_file_name = "school_data.xlsx"
df_data_to_write.to_excel(excel_file_name, index = False)


'''
Task to do:
change column names in line number 36:
--------- columns =['ID', 'Place', 'District', 'Division', 'Area', 'Population' -------
according to your table's columns and create your own excel report.

You can also change the filename in line 37 but it is not mandatory.
'''
