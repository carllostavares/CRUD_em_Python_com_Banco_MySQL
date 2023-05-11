import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    password ='Wlwl2350@Ju' ,
    database = 'bd_lista_vendas',
)
cursor = conexao.cursor()

#CRUD
id_cpf_cliente = "111.222.333-44"
nome_cliente =  "Carlos Tavares"
nome_porduto = "Pizza"
valor_venda = 70.50

comando = f'INSERT INTO tb_vendas (id_cpf_cliente,nome_cliente,nome_porduto,valor_venda) VALUES ("{id_cpf_cliente}","{nome_cliente}",' \
f'"{nome_porduto}",{valor_venda})'

cursor.execute(comando)
conexao.commit() #adita o banco de dados
#resultado = cursosr.fecthall() #ler o banco de dados

cursor.close()
conexao.close()

#CREATE
#READ
#UPDATE
#DELETE