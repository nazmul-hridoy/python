'''
We have a database at db4free.net which we can browse using this link:
https://www.db4free.net/phpmyadmin.php

This code will connect to that database but will not do anything.
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
connection.close()