class Endereco():

    def __init__(self, CEP, numCasa, estado):
        self.CEP = CEP
        self.numCasa = numCasa
        self.estado = estado
        self.cidade = None
        self.bairro = None
        self.rua = None

    def __str__(self):
        return f'{self.CEP}-{self.estado}-{self.numCasa}'

    def addCidade(self, cidade):
        self.cidade = cidade

    def addBairro(self, bairro):
        self.bairro = bairro

    def addRua(self, rua):
        self.rua = rua
