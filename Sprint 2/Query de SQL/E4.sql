select autor.codautor, autor.nome, autor.nascimento, count(livro.autor) as quantidade 
from autor
left join livro
	on livro.autor = autor.codautor
group by autor.nome
order by autor.nome
