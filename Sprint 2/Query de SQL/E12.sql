with somatorio_vendas as (
	select SUM(tbvendas.qtd*tbvendas.vrunt) as valor_total_vendas, tbvendas.cdvdd
  	from tbvendas
  	where status = 'Concluído'
  	group by cdvdd
)
select tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc, somatorio_vendas.valor_total_vendas
from tbvendedor 
left join somatorio_vendas
	on somatorio_vendas.cdvdd = tbvendedor.cdvdd
left join tbdependente
	on tbdependente.cdvdd = tbvendedor.cdvdd
where somatorio_vendas.valor_total_vendas = (
	SELECT MIN(somatorio_vendas.valor_total_vendas)
  	FROM somatorio_vendas
)
GROUP BY tbvendedor.cdvdd
