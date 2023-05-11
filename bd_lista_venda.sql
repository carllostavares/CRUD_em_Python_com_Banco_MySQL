CREATE SCHEMA bd_lista_vendas; 

CREATE TABLE tb_vendas (
id_cpf_cliente VARCHAR(14) NOT NULL,
id_vendas INT NOT NULL AUTO_INCREMENT,	
nome_cliente VARCHAR(200) NOT NULL,
nome_porduto VARCHAR(45) NOT NULL,
valor_venda decimal(7,2) ZEROFILL NOT NULL,

PRIMARY KEY (id_vendas )) ;