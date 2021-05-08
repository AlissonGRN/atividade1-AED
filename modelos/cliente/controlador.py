from modelos.cliente.cliente import Cliente
from modelos.cliente.daoCliente import DaoCliente


class ControladorCliente():

    def __init__(self):
        self.__dao = DaoCliente()

    def menu(self):
        print('-' * 10)
        print('1 -  Cadastar')
        print('2 -  Buscar por CPF')
        print('3 -  Listar todos')
        print('4 -  Listar por estado')
        print('0 -  Sair')

    def cadastarCliente(self):
        print('Cadastro de cliente')
        nome = input('Nome do Cliente: ')
        cpf = input('CPf do Cliente: ')
        if self.__dao.salvarCliente(Cliente(nome, cpf)):
            print(f'Cliente {nome} adicionado')
        else:
            print('Cliente já existe')

    def listarClientes(self):
        clientes = self.__dao.listarClientes()
        for cliente in clientes:
            print(cliente)

    def buscarPorCPF(self):
        clientes = self.__dao.listarClientes()
        cpfCliente = input('Digite o cpf: ')
        for cliente in clientes:
            if cliente.cpf == cpfCliente:
                print(f'{cliente.nome} - {cliente.cpf}')

    def iniciarSistema(self):
        while True:
            self.menu()
            opcao = input('Digite uma opção: ')

            if opcao == '1':
                self.cadastarCliente()
            elif opcao == '2':
                self.buscarPorCPF()
            elif opcao == '3':
                self.listarClientes()
            elif opcao == '4':
                print('Ainda não implementado')
            elif opcao == '0':
                input('Saindo do sistema - digite enter')
                return
            else:
                print('Opção invalida, tente novamente')
