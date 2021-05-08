class Venda():

    def __init__(self, codigo, cliente):
        self.codigo = codigo
        self.cliente = cliente
        self.produtos = []

    def temProdutos(self):
        if len(self.produtos) > 0:
            return True
        return False

    def addProduto(self, produto):
        self.produtos.append(produto)
