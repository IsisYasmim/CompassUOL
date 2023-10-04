select * from tb_locacao

/* 1FN - criando novas tabelas para atributos multivalorados */

CREATE TABLE tb_kmCarro(
  	idcarro INT,
  	kmCarro INT
)

INSERT INTO tb_kmCarro(idcarro, kmCarro)
SELECT idCarro, kmCarro
FROM tb_locacao

ALTER TABLE tb_locacao
DROP COLUMN kmcarro

select * from tb_kmCarro

/* 2FN - criando tabelas para atributos que só dependem de outros ids*/

CREATE TABLE tb_cliente(
	idCliente INT PRIMARY KEY,
  	nomeCliente VARCHAR(100),
  	cidadeCliente VARCHAR(40),
  	estadoCliente VARCHAR(40),
  	paisCliente VARCHAR(40)
)
INSERT INTO tb_cliente
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao

SELECT * from tb_cliente

ALTER TABLE tb_locacao DROP COLUMN nomecliente
ALTER TABLE tb_locacao DROP COLUMN cidadecliente
ALTER TABLE tb_locacao DROP COLUMN estadocliente
ALTER TABLE tb_locacao DROP COLUMN paiscliente


CREATE TABLE tb_carro(
	idcarro INT PRIMARY KEY,
  	classicarro VARCHAR(50),
  	marcacarro VARCHAR(80),
  	modelocarro VARCHAR(80),
 	anocarro INT,
  	idcombustivel INT,
  	tipocombustivel VARCHAR(20)
)
INSERT INTO tb_carro
SELECT DISTINCT idcarro, classicarro, marcacarro, modelocarro, anocarro, idcombustivel, tipocombustivel
from tb_locacao

SELECT * from tb_carro 

ALTER TABLE tb_locacao DROP COLUMN classicarro
ALTER TABLE tb_locacao DROP COLUMN marcacarro
ALTER TABLE tb_locacao DROP COLUMN modelocarro
ALTER TABLE tb_locacao DROP COLUMN anocarro
ALTER TABLE tb_locacao DROP COLUMN idcombustivel
ALTER TABLE tb_locacao DROP COLUMN tipocombustivel

CREATE TABLE tb_vendedor(
	idvendedor INT PRIMARY KEY,
  	nomevendedor VARCHAR(15),
  	sexovendedor SMALLINT,
  	estadovendedor VARCHAR(40)
)
INSERT INTO tb_vendedor
SELECT DISTINCT idvendedor, nomevendedor, sexovendedor, estadovendedor
from tb_locacao

ALTER TABLE tb_locacao DROP COLUMN nomevendedor
ALTER TABLE tb_locacao DROP COLUMN sexovendedor
ALTER TABLE tb_locacao DROP COLUMN estadovendedor


/* 3FN - criando tabelas para atributos que dependem de outros atributos*/

CREATE TABLE tb_combustivel(
	idcombustivel INT PRIMARY KEY,
  	tipocombustivel VARCHAR(20)
)
insert into tb_combustivel
SELECT DISTINCT idcombustivel, tipocombustivel
from tb_carro

ALTER TABLE tb_carro DROP COLUMN tipocombustivel
SELECT * from tb_combustivel

select * from tb_locacao