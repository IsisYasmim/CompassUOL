select tbvendas.cdpro, nmpro, nmcanalvendas, SUM(qtd) as quantidade_vendas
from tbvendas
where status = 'Concluído' 
group by tbvendas.cdpro, tbvendas.cdcanalvendas
order by quantidade_vendas 
limit 10