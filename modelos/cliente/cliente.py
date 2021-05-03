class Cliente():

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.endereco = None
        self.contatos = []

    def __str__(self):
        return f'{self.nome}-{self.cpf}'

    def temContatos(self):
        if len(self.contatos) > 0:
            return True
        return False

    def addContato(self, contato):
        self.contato.append(contato)