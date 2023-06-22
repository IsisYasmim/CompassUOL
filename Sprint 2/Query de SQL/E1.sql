select cod, titulo, autor, editora, valor, publicacao, edicao, idioma
from livro
where publicacao > '2014-12-31'
order by cod