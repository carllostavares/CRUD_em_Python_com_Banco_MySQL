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
#comando = f'SELECT * FROM  tb_vendas'
#cursor.execute(comando)
#conexao.commit() #adita o banco de dados
#resultado = cursor.fetchall() #ler o banco de dados
#print(resultado)

#cursor.close()
#conexao.close()

#UPDATE
#nome_produto = "bolo"
#valor_venda = 200.50

#comando = f'UPDATE tb_vendas SET valor_venda = {valor_venda} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()

#cursor.close()
#conexao.close()

#DELETE

nome = "Pedro"

comando = f'DELETE FROM tb_cliente WHERE nome = "{nome}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
