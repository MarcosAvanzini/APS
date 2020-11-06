import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='Login',
                                        user='root',
                                        password='Amofamilia123@')
    
    mySql_Create_Table_Query = """SELECT * FROM LoginAps"""
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    for i in cursor.fetchall():
        print(bytes.fromhex(i[2]))
    

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")