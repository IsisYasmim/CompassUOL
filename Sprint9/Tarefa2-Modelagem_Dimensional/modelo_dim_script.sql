CREATE VIEW dim_DataEntrega AS
SELECT dataEntrega AS dataEntrega,
	   horaEntrega
FROM tb_locacao tl;

CREATE VIEW dim_DataLocacao AS
SELECT dataLocacao,
	   horaLocacao
FROM tb_locacao tl;

CREATE VIEW dim_Cliente AS
SELECT idCliente,
	   nomeCliente,
	   cidadeCliente,
	   estadoCliente,
	   paisCliente
FROM tb_cliente tc;

CREATE VIEW dim_Vendedor AS
SELECT idvendedor AS idVendedor,
	   nomeVendedor,
	   sexoVendedor,
	   estadoVendedor
FROM tb_vendedor tv;

CREATE VIEW dim_Carro AS
SELECT tc.idCarro,
	   tcom.tipocombustivel,
	   tkc.kmCarro,
	   tc.classicarro,
	   tc.anocarro,
	   tc.marcacarro,
	   tc.modelocarro,
	   tc.marcacarro
FROM tb_carro tc 
JOIN tb_combustivel tcom ON tcom.idcombustivel = tc.idcombustivel
JOIN tb_kmCarro tkc ON tkc.idcarro  = tc.idCarro;

CREATE VIEW fato_LocacaoVenda AS
SELECT tl.idLocacao,
	   tl.qtdDiaria,
	   tl.vlrDiaria,
	   tc.idcarro,
	   tcli.nomeCliente,
	   tv.nomevendedor,
	   ddl.dataLocacao,
	   dde.dataEntrega
FROM tb_locacao tl 
JOIN tb_carro tc ON tc.idcarro = tl.idCarro
JOIN tb_cliente tcli ON tcli.idCliente = tl.idCliente
JOIN tb_vendedor tv ON tv.idvendedor = tl.idVendedor
JOIN dim_DataLocacao ddl ON ddl.dataLocacao = tl.dataLocacao
JOIN dim_DataEntrega dde ON dde.dataEntrega = tl.dataEntrega;

