from teste import *


if __name__ == '__main__':
    conexao = conectar('localhost', 'aula', '3223', 'py_mysql')
    listar(conexao)
