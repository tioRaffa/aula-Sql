'''
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='....',
    password='....',
    database='qual banco de dados'
)

___________________________________________

cursor = conexao.cursor()

comando = ' ' \ ESCREVER O COMANDO SQL
cursor.execute(comando)

cursos.fetchall() \ serve para ler
cursor.commit() \ serva para CREAT, UPDATE, DELETE


'''
