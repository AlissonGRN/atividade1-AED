class Client:

    def __init__(self, name, cpf):

        self.__name = name
        self.__cpf = cpf
        self.__address = None
        self.__contacts = []

    def getName(self):
        return self.__name

    def getCPF(self):
        return self.__cpf

    def getEndereco(self):
        return self.__address

    def getContatos(self):
        return self.__contacts

    def hasContacts(self):
        if len(self.__contacts) > 0:
            return True
        return False

    def addContact(self, contact):
        self.__contacts.append(contact)