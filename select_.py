'''
WHERE id in (1, 2, 4.....)

WHERE nome LIKE 'a%' comeca com
                '%a' termina com
                
WHERE created_at BETWEEN '2020-02-28' AND '2021-08-30'     BETWEEN ( ENTRE )

_________________________________________________________________________________

SELECT * FROM cliente
LEFT OUTER JOIN profissoes
ON cliente.id_profissao = profissoes.id;

SELECT * FROM cliente
RIGHT OUTER JOIN profissoes
ON cliente.id_profissao = profissoes.id;
####################

SELECT AVG(preco_venda) FROM product;           CALCULA A MEDIA
SELECT ROUND(AVG(preco_venda), 3) FROM product;
MAX / MIN

______//_____________//_____________//___________//

MOSTRA OS MAIORES PRECOS DE CADA CATEGORIA

SELECT id_categoria, MAX(descricao) AS 'Descricao',          AGREGACAO
ROUND(MAX(preco_venda), 3) AS 'PRECO MAXIMO'
FROM product
GROUP BY id_categoria

_____________


'''
