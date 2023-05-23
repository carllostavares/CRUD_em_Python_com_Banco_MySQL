import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    password ='Wlwl2350@Ju' ,
    database = 'bd_lista_vendas',
)
cursor = conexao.cursor()


#CREATE
""" id_cpf_cliente = "878.222.333-00"
nome_cliente =  "Nathalia Salles"
nome_produto = "biscoito"
valor_venda = 8.90

comando = f'INSERT INTO tb_vendas (id_cpf_cliente,nome_cliente,nome_produto,valor_venda) VALUES ("{id_cpf_cliente}","{nome_cliente}",' \
f'"{nome_produto}",{valor_venda})'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close() """

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
#conexao.commit() #a

#cursor.close()
#conexao.close()

#DELETE
nome_cliente = "Rodrigo Gomes"

comando = f'DELETE FROM tb_vendas WHERE nome_cliente = "{nome_cliente}"'
cursor.execute(comando)
conexao.commit()

