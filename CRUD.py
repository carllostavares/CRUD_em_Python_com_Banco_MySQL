import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    password ='Wlwl2350@Ju' ,
    database = 'bd_lista_vendas',
)
cursor = conexao.cursor()

#CRUD

cursor.close()
conexao.close()

#CREATE
#READ
#UPDATE
#DELETE