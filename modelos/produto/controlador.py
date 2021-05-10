from modelos.produto.produto import Produto
from modelos.produto.daoProduto import DaoProduto


class ControladorProduto():

    def __init__(self):
        self.__dao = DaoProduto()

    def menu(self):
        print('-' * 10)
        print('1 - Cadastrar')
        print('2 - Buscar por codigo')
        print('3 - Listar todos')
        print('0 - Sair')

    def cadastarProduto(self):
        print('Cadastro de produto')
        codigo = input('Digite o codigo do produto: ')
        nome = input('Digite o nome do produto: ')
        valor = input('Digite o valor do produto: ')
        if self.__dao.salvarProduto(Produto(codigo, nome, valor)):
            print(f'produto {nome} adicionado')
        else:
            print('Produto já existe')

    def listarProdutos(self):
        produtos = self.__dao.listarProdutos()
        for produto in produtos:
            print(produto)

    def buscarPorCodigo(self):
        produtos = self.__dao.listarProdutos()
        codigoProduto = input('Digite o codigo: ')
        for produto in produtos:
            if produto.codigo == codigoProduto:
                print(f'{produto.nome}-{produto.valor}')

    def iniciarSistema(self):
        while True:
            self.menu()
            opcao = input('Digite uma opção: ')

            if opcao == '1':
                self.cadastarProduto()
            elif opcao == '2':
                self.buscarPorCodigo()
            elif opcao == '3':
                self.listarProdutos()
            elif opcao == '0':
                input('Saindo do sistema - digite enter')
                return
            else:
                print('opção invalida, tente novamente')
