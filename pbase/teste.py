from pickle import FALSE, TRUE
import mysql.connector
from mysql.connector import Error


def conectar(host_, user_, password_, database_):
    conectado = FALSE

    try:
        conexao = mysql.connector.connect(
            host=f'{host_}',
            user=f'{user_}',
            password=f'{password_}',
            database=f'{database_}'
        )
        conectado = TRUE
    except Error as e:
        print('Erro de conexao com o Banco de Dados')
        raise e
    finally:
        if conectado is TRUE:
            print('Banco de Dados conectado!')
            return conexao
        else:
            return None


def listar(cnx):
    conexao = cnx
    cursor = conexao.cursor()

    comando = 'SELECT * FROM produto'
    try:
        cursor.execute(comando)
        produtos = cursor.fetchall()

        if len(produtos) > 0:
            print('~='*15)
            for p in produtos:
                print(f'ID: {p[0]}')
                print(f'Nome: {p[1]}')
                print(f'Preco: R${p[2]}')
                print(f'Estoque: {p[3]}')
                print('~='*15)
            print('')
        else:
            print('\033[31mNenhum produto inserido no Banco de Dados!\033[m')
    except Exception as e:
        print('Erro, tente novamente.')
        print(f'Detalhe do ERRO -> {e}')
    finally:
        conexao.close()
        cursor.close()


def inserir(cnx):
    conexao = cnx
    cursor = conexao.cursor()

    try:
        nome_produto = input('Produto -> ')
        preco = float(input('Preco produto -> R$'))
        estoque = int(input('Quantidade em estoque ->'))

        comando = 'INSERT INTO produto (nome, preco, estoque) VALUES (%s, %s, %s)'

        cursor.execute(comando, (nome_produto, preco, estoque))
        conexao.commit()

        if cursor.rowcount == 1:
            print(f'Produto {nome_produto} inserido com sucesso no BD!')
        else:
            print('Erro ao inserir o produto no BD!')
    except Exception as e:
        print(f'Erro: {e}')
    except ValueError as e:
        print(f'Erro: {e}')
    finally:
        conexao.close()
        cursor.close()


def update(cnx):
    conexao = cnx
    cursor = conexao.cursor()

    try:
        id_produto = int(input('ID do Produto a ser alterado -> '))
        novo_nome = input('Novo nome -> ')
        novo_preco = float(input('Novo preco -> R$'))
        novo_estoque = int(input('Quantidade em Estoque -> '))

        comando = 'UPDATE produto SET nome = %s, preco = %s, estoque = %s WHERE id = %s'

        cursor.execute(comando, (novo_nome, novo_preco,
                       novo_estoque, id_produto))
        conexao.commit()

        if cursor.rowcount == 1:
            print(f'Produto com ID: {id_produto} alterado com sucesso!')
        else:
            print(f'Nenhum produto com ID: {id_produto} foi encontrado')
    except Exception as e:
        print(f'Erro ao atualizar o produto: {e}')
    finally:
        conexao.close()
        cursor.close()
