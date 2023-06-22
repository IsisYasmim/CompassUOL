select autor.nome
from autor
left join livro
	on livro.autor = autor.codautor
group by autor.nome
having count(livro.autor) = 0
order by autor.nome