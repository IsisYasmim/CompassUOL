with somatorio_vendas as (
	select SUM(qtd * vrunt) as gasto, cdcli
 	from tbvendas
  	where status = 'Concluído'
  	group by cdcli
)

select tbvendas.cdcli, tbvendas.nmcli, somatorio_vendas.gasto
from tbvendas
left JOIN somatorio_vendas
	on tbvendas.cdcli = somatorio_vendas.cdcli
WHERE somatorio_vendas.gasto = (
	SELECT MAX(gasto)
	FROM somatorio_vendas
)
group by tbvendas.cdcli
order by somatorio_vendas.gasto desc