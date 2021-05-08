from modelos.cliente.controlador import ControladorCliente
from modelos.venda.controlador import controladorVenda


class Sistema():

    def __init__(self):
        self.controladorCliente = ControladorCliente()
        self.controladorVenda = controladorVenda()

    def menuPrincipal(self):
        print('-=-' * 5)
        print('1 - Cliente')
        print('2 - Produto')
        print('3 - Venda')
        print('0 - Sair')
        print('-=-' * 5)

    def iniciar(self):
        while True:
            self.menuPrincipal()
            opcao = input('Digite uma opção: ')
            if opcao == '1':
                self.controladorCliente.iniciarSistema()

            elif opcao == '2':
                pass
            elif opcao == '3':
                self.controladorVenda.iniciarSistema()
            elif opcao == '0':
                input('Saindo do sistema - digite enter')
                return
            else:
                print('Opção invalida, tente novamente')
