'''
Here we will first read data from an existing excel file: data.xlsx
And print them in the console to re-check the values
Then we will insert these values in the table using for loop
Finally we will browe the database table in phpmyadmin and check the inserted values
'''
import pandas as pd
import mysql.connector
import time
'''
Create Connection
'''


connection = mysql.connector.connect(host='db4free.net',
                                         database='nazmul',
                                         user= 'nazmul',
                                         password= '123456789',
                                         autocommit = True)
cursor = connection.cursor()

'''
Create an excel file with the exact columns as your database table and insert some lines.
Next, we will read from the excel file, as for example: data.xlsx
'''
data = pd.read_excel('school_data.xlsx')
print(data)

'''
Insert these values into pnt_python database, locatoin_taw table
'''

for index, value in data.iterrows():
    
    School_id = None;
    School_name = str(data['school name'][index]);
    Main_brunch= str(data['main brunch'][index]);
    Total_class= str(data['total classs'][index]);
    Total_student= str(data['total student'][index]);
    Total_brunch= str(data['total brunch'][index]);
    
    variable_values = (School_id, School_name, Main_brunch, Total_brunch, Total_student, Total_brunch)
    mySql_insert_query = """INSERT INTO table_school
                            (School_id, School_name, Main_brunch, Total_class, Total_student, Total_brunch) 
                                VALUES 
                            (%s, %s, %s, %s, %s, %s) """
    
    cursor.execute(mySql_insert_query, variable_values)
    print(index)
    # sleep(2)

cursor.close()

'''
Now go to https://www.db4free.net/phpmyadmin.php and browse your table and see the changes.
'''