class Conta:
    def __init__ (self, clientes, numero, telefone, saldo = 0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.telefone = telefone
        self.operacoes = []
    def resumo(self):
        print("CC Número: %s \n Saldo: %.2f \n Nome: %s \n Telefone: %s " %
              (self.numero, self.saldo, self.clientes, self.telefone))
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["Saque", valor])
        else:
            print("Saldo Insuficiente")
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO: ", valor])
    def extrato(self):
        print("Extrato CC N %s\n" % self.numero)
        for i in self.operacoes:
            print("%10s %10.2f" % (i[0], i[1]))
        print("\n Saldo: %10.2f\n" % self.saldo)
        
    
