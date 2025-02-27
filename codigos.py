'''
__________________________________________________________
CREATE TABLE 'nome da tabela'(
    id INT NOT NUL AUTO_INCREMENT PRIMARY KEY,              criando tabela
EX: nome VARCHAR(45) NOT NULL 
);

INSERT INTO 'nome da tabela' (nome) VALUES('rafael');      inserindo na tabela

_________________________________________________________________________________
SELECT * FROM (nome_tabela) WHERE (campo) = 1;             buscando na tabela
AND ....
_________________________________________________________________________________


UPDATE 'nome da tabela' SET nome = 'novo nome' WHERE id = 1;     alterando a tabela


DELETE FROM 'nome da tabela' WHERE 'nome do campo' = 0;          deleta as info do campo 0 da tabela

ALTER TABLE pagamentos ADD COLUMN salario MONEY NOT NULL; POSTGRE------------

ALTER TABLE 'nome da tabela' ADD 'novo valor' INT / VARCHAR()... ;  adiciona um novo campo na tabela

DROP TABLE 'nome da tabela';                                        APAGA A TABELA


BOAS PRATICAS

SELECT 
    a.nome AS Produto,
    a.fabricante,
    a.validade,
    d.cnpj AS CNPJ_DISTRIBUIDORA,
    d.veiculo,
    m.nome AS Motorista,
    m.idade,
    m.ano_nascimento AS Nascimento,
    m.categoria,
    m.salario
FROM
    alimentos AS a
JOIN
    distribuidora AS d ON a.id_distribuidora = d.id
JOIN 
    motorista as m ON d.id_info_motorista = m.id
WHERE
    m.idade >= 23;

____________________________________________________________

postgre  mysql (START...)
  |
BEGIN TRANSACTION;      inicia a transicao
    codigo...

COMMIT;  salva definitio as alteracoes

ROLLBACK;   remove as alteracoes feitas no BEGIN TRANSACTION
 


'''
