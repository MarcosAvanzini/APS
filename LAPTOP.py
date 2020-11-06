import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='APS',
                                         user='root',
                                         password='Amofamilia123@')

    mySql_Create_Table_Query = """CREATE TABLE Login ( 
                             Usuario varchar(250) NOT NULL,
                             Senha varchar(250) NOT NULL,
                             PRIMARY KEY (Usuario)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
