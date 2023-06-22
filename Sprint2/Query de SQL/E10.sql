with valortotal as (
	SELECT SUM(qtd * vrunt) as valortotal, cdvdd
 	from tbvendas
  	where tbvendas.status like 'Concluído'
 	group by cdvdd
) 

select 
	tbvendedor.nmvdd as vendedor,
	ROUND(valortotal.valortotal, 2) AS valor_total_vendas, 
	ROUND((valortotal.valortotal * tbvendedor.perccomissao) / 100, 2) as comissao

from tbvendedor
left join tbvendas
	on tbvendedor.cdvdd = tbvendas.cdvdd
    
LEFT JOIN valortotal AS valortotal 
    ON tbvendas.cdvdd = valortotal.cdvdd
    
where tbvendas.status like 'Concluído'
group by vendedor
order by comissao desc
