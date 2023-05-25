import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    password ='Wlwl2350@Ju' ,
    database = 'fim_de_feira',
)

cursor = conexao.cursor()

""" #CREATE
id_cpf_cliente = "000.000.111-00"
nome = "Joao Carlos"
sobrenome = "Gomes"
email = "testando@teste.com"
sexo = "M"
data_nasc = '1996-07-09'
senha = "19191919"
id_numero = 2
numero = "84988293122"

comando = f'call inserir_cliente("{id_cpf_cliente}","{nome}","{sobrenome}","{email}","{sexo}","{data_nasc}","{senha}","{id_numero}","{numero}")'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
 """
#READ
""" nome = "Pedro"
comando = f'SELECT * FROM tb_cliente where nome = "{nome}"'
cursor.execute(comando)
resultado = cursor.fetchall() #ler o banco de dados
print(resultado)

cursor.close()
conexao.close() """

#UPDATE
""" nome = "carlos"
email = "EMAILCORRETO@HOTMAIL.COM"

comando = f'UPDATE tb_cliente SET email = "{email}" WHERE nome = "{nome}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
 """
""" #DELETE

nome = "Pedro"

comando = f'DELETE FROM tb_cliente WHERE nome = "{nome}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
 """