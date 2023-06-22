select editora.nome, count(livro.editora) as quantidade, endereco.estado, endereco.cidade

from livro 
left join editora 
	on livro.editora = editora.codeditora
left join endereco
	on endereco.codendereco = editora.endereco
group by editora.nome
order by quantidade desc
limit 5