from logging import raiseExceptions
from os import error
from pickle import FALSE, TRUE
from mysql.connector import Error
import mysql.connector


def mn():
    from time import sleep
    print('Conectando ao servidor', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')


def conectar(host, user, password, database):
    mn()
    conectado = FALSE
    try:
        cnx = mysql.connector.connect(
            host=f'{host}',
            user=f'{user}',
            password=f'{password}',
            database=f'{database}'
        )
        conectado = TRUE
    except Error as e:
        conectado = FALSE
        print(f'\033[31mErro na Conexao com o Banco de Dados\033[m')
        raise e
    finally:
        if conectado is TRUE:
            print('Banco de Dados conectado com sucesso!')
            print('\n')
            return cnx
        else:
            return None


def desconectar(conexao):
    print('Desconectando do servidor...')
    try:
        if conexao:
            conexao.close()
            print('\033[31mdesconectado\033[m')
    except:
        if conexao is None:
            print('Nenhuma Conexão!')


def listar(cnx):
    conexao = cnx
    # ____
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM produto;')
    produto = cursor.fetchall()

    if len(produto) > 0:
        print('Listando produtos...')
        for p in produto:
            print(f'ID -> {p[0]}')
            print(f'Nome -> {p[1]}')
            print(f'Preco -> {p[2]}')
            print(f'Estoque -> {p[3]}')
            print('\n')
    else:
        print('\033[31mNAO EXISTE PRODUTOS CADASTRADOS\033[m')
    desconectar(conexao)


def inserir(cnx):
    conexao = cnx
    cursor = conexao.cursor()

    try:
        nome = input('Nome do Produto -> ')
        preco = float(input('Preco do Produto -> '))
        estoque = int(input('Quantidade em Estoque -> '))

        comando = 'INSERT INTO produto (nome, preco, estoque) VALUES (%s, %s, %s)'
        cursor.execute(comando, (nome, preco, estoque))
        conexao.commit()

        if cursor.rowcount == 1:
            print(f'Produto {nome} Adicionado com sucesso!')
        else:
            print('Nao foi possivel inserir o produto!')

    except ValueError as e:
        print(f'Erro: {e}')
    except Exception as e:
        print('Erro, Tente inserir os dados novamente!')
        print(f'Detalhes do erro: {e}')

    finally:
        cursor.close()
        conexao.close()


def atualizar(cnx):
    conexao = cnx
    cursor = conexao.cursor()

    try:
        id_produto = int(input('Codigo do produto -> '))
        nv_nome = input('Novo nome -> ')
        nv_preco = float(input('Novo preco -> '))
        nv_estoque = int(input('Novo qntd de Estoque -> '))

        comando = "UPDATE produto SET nome = %s, preco = %s, estoque = %s WHERE id = %s"
        cursor.execute(comando, (nv_nome, nv_preco, nv_estoque, id_produto))
        conexao.commit()

        if cursor.rowcount == 1:
            print(f'O produto com ID {id_produto} foi atualizado com sucesso!')
        else:
            print(f'Nenhum produto com ID {
                  id_produto} encontrado para atualizar.')

    except Exception as e:
        print(f"Erro ao atualizar o produto: {e}")

    finally:
        cursor.close()
        conexao.close()


def deletar():
    """
    Função para deletar um produto
    """
    print('Deletando produto...')


def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
