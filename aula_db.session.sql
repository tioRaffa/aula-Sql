INSERT INTO carinho_filmes (id_dvd, id_cliente)
VALUES(
    (SELECT id FROM dvd WHERE id_filme = (SELECT id FROM filme WHERE titulo LIKE 'Coringa')),
    (SELECT id FROM cliente WHERE nome LIKE 'Rafa%')
),
(
    (SELECT id FROM dvd WHERE id_filme = (SELECT id FROM filme WHERE titulo LIKE 'Matrix')),
    (SELECT id FROM cliente WHERE nome LIKE 'Rafa%')
);