class DaoVenda():

    def __init__(self):
        self.vendas = []

    def buscarVenda(self, codigo):
        for venda in self.vendas:
            if venda.codigo == codigo:
                return venda
        return None

    def salvarVenda(self, venda):
        if self.buscarVenda(venda.codigo) is None:
            self.vendas.append(venda)
            return True
        return False

    def listarVendas(self):
        return self.vendas.copy()
