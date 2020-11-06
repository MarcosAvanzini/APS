def loginAPS():
    import mysql.connector
    from mysql.connector import Error
    from Encriptador import login
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='Login',
                                            user='root',
                                            password='Amofamilia123@')
        
        mySql_Create_Table_Query = """INSERT INTO LoginAps ( 
                                Usuario, Senha, SenhaENC) VALUES ('%s','%s' ,'%s');""" % (input("Digite seu Usuario: "),input('Digite Sua Senha: '),login().hex())

        cursor = connection.cursor()
        cursor.execute(mySql_Create_Table_Query)
        connection.commit()
        print("Cadastro Criado Com sucesso!!")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        connection = mysql.connector.connect(host='localhost',
                                            database='Login',
                                            user='root',
                                            password='Amofamilia123@')
        if (connection.is_connected()):
            cursor = connection.cursor()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    

