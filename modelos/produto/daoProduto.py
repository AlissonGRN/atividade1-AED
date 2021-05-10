class DaoProduto():

    def __init__(self):
        self.produtos = []

    def buscarProduto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def salvarProduto(self, produto):
        if self.buscarProduto(produto.codigo) is None:
            self.produtos.append(produto)
            return True
        return False

    def listarProdutos(self):
        return self.produtos.copy()
