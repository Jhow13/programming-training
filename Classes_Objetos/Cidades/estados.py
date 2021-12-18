class Estado:
    def __init__ (self, nome, sigla, total = 0):
        self.sigla = sigla
        self.nome = nome
        self.cidades = []
        self.total = 0

    def resumo(self):
        print("Nome: %s \nSigla: %s" % (self.nome, self.sigla))
        
    def inseri_cidade(self, cidade, populacao):
        self.total += populacao
        self.cidades.append([cidade, populacao])
        
    def lista_cidades(self):
        for i in self.cidades:
            print("Cidade: %s \nPopulação: %s" % (i[0], i[1]))
        print("Total de população em %s -%s: %s" % (self.nome, self.sigla, self.total))
        
