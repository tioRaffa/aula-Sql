from utils import *

if __name__ == '__main__':
    cnx = conectar(host='localhost', user='teste',
                   password='teste', database='pypostgre')
    # inserir(cnx, 'Playstation 5', '4500', 10)
    # inserir(cnx, 'Xbox Series X', '4500', 10)
    # atualizar(cnx)
    listar(cnx)
