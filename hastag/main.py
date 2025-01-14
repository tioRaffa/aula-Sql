import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='aula',
    password='3223',
    database='bdhastag'
)

cursor = conexao.cursor()

comando = 'INSERT INTO vendas (nome, preco) VALUES("Bmx", "3589")'
cursor.execute(comando)
conexao.commit()

conexao.close()
cursor.close()
