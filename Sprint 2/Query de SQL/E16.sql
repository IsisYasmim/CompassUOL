select tbvendas.estado, tbvendas.nmpro, ROUND(AVG((tbvendas.qtd)), 4) as quantidade_media
from tbvendas
where status = 'Concluído'
group by tbvendas.estado, tbvendas.nmpro
order by tbvendas.estado, tbvendas.nmpro