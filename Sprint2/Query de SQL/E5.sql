SELECT DISTINCT autor.nome
FROM autor
JOIN livro ON autor.codautor = livro.autor
JOIN editora ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
WHERE endereco.estado NOT LIKE 'RIO GRANDE DO SUL' and endereco.estado not like 'PARANÁ' and endereco.estado not like 'SANTA CATARINA'
  
ORDER BY autor.nome 