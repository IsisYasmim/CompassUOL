select tbvendedor.cdvdd, tbvendedor.nmvdd
from tbvendedor
left join tbvendas
	on tbvendedor.cdvdd = tbvendas.cdvdd
group by tbvendedor.nmvdd
HAVING COUNT(tbvendas.cdvdd) = (
    SELECT MAX(contagem_venda)
    FROM (
        SELECT COUNT(tbvendas.cdvdd) as contagem_venda
        FROM tbvendas
        GROUP BY tbvendas.cdvdd
    ) as vendas
 )
order by tbvendedor.nmvdd