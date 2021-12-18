class Cidade:
    def __init__ (self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
    def resumo(self):
        print("Nome: %s \n População: %s" % (self.nome, self.populacao))
