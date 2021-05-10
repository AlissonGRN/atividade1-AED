class Produto():

    def __init__(self, codigo, nome, valor):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f'{self.codigo}-{self.nome}-{self.valor}'
