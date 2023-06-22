select autor.codautor, autor.nome, count(livro.autor) as quantidade_publicacoes
from autor
left join livro
	on livro.autor = autor.codautor
group by autor.nome
HAVING COUNT(livro.autor) = (
    SELECT MAX(quantidade_publicacoes)
    FROM (
        SELECT COUNT(livro.autor) as quantidade_publicacoes
        FROM autor
        LEFT JOIN livro ON livro.autor = autor.codautor
        GROUP BY autor.codautor
    ) as publicacoes
)
order by quantidade_publicacoes DESC
