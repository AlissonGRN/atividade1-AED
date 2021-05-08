from modelos.venda.venda import Venda
from modelos.venda.daoVenda import DaoVenda
from modelos.cliente.daoCliente import DaoCliente
from modelos.produto.produto import Produto


class controladorVenda():

    def __init__(self):
        self.__daoVenda = DaoVenda()
        self.__daoCliente = DaoCliente()

    def menu(self):
        print('-' * 10)
        print('1 - Cadastar')
        print('2 - Buscar por codigo')
        print('3 - Listar todos')
        print('4 - Listar venda por cliente')  # POR CPF DO CLIENTE
        # TOTAL DE VENDAS NO SISTEMA
        print('5 - Listar todas as vendas por estado')
        print('6 - Total de vendas no sistema')
        print('7 - Total de produtos vendidos')
        print('8 - Total de produtos vendidos')
        print('9 - Valor total de vendas')
        print('0 - Sair')

    def cadastarVenda(self):
        print('Cadastro de venda')
        codigo = input('Codigo da venda')
        cpfCliente = input('Digite o CPF do cliente: ')
        if self.__daoCliente.buscarCliente(cpfCliente) is not None and self.__daoVenda.buscarVenda(codigo) is None:
            pass

    def addProduto(self, produto):
        self.__daoVenda.produtos.append(produto)

    def listarVendaCliente(self):
        print('não implementado')

    def iniciarSistema(self):
        while True:
            self.menu()
            opcao = input('Digite uma opção: ')

            if opcao == '1':
                self.cadastarVenda()
            elif opcao == '2':
                self.buscarVenda()
            elif opcao == '3':
                self.listarVendas()
            elif opcao == '4':
                self.listarVendaCliente()
            elif opcao == '5':
                print("não implementado")
            elif opcao == '0':
                input('saindo do sistema - aperte enter')
                return
            else:
                print('opção desconhecida, por favor tente novamente')
