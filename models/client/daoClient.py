class DaoClient():

    def __init__(self):
        self.__clients = []

    def addClient(self, client):
        client = self.searchClient(client.cpf)
        if client is None:
            self.__clients.append(client)
            return True
        return False

    def searchClient(self, cpf):
        for client in self.__clients:
            if client.cpf == cpf:
                return client
        return None
