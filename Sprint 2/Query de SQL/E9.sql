select tbestoqueproduto.cdpro, tbvendas.nmpro
from tbestoqueproduto
left join tbvendas
	on tbvendas.cdpro = tbestoqueproduto.cdpro
where tbvendas.dtven BETWEEN '2014-02-03' and '2018-02-02' and tbvendas.status like 'Concluído'
group by tbvendas.cdpro
having COUNT(tbvendas.cdpro) = (
	SELECT MAX(contagem_produto)
  	from (
    	SELECT COUNT (tbvendas.cdpro) as contagem_produto
      	from tbvendas
      	WHERE tbvendas.dtven BETWEEN '2014-02-03' AND '2018-02-02' 
       AND tbvendas.status LIKE 'Concluído'
      	GROUP by tbvendas.cdpro
    ) as contagem
)
order by tbvendas.cdpro