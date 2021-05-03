class DaoCliente():

    def __init__(self):
        self.clientes = []

    def buscarCliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return none

    def salvarCliente(self, cliente):
        if self.buscarCliente(cliente.cpf) is None:
            self.clientes.append(cliente)
            return True
        return False

    def listarClientes(self):
        return self.clientes.copy()
