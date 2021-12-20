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
            self.operacoes.append(["SAQUE: ", valor])
            return "Saque Efetuado com sucesso!"
        else:
            return "Saldo Insuficiente"
            
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO: ", valor])
    def extrato(self):
        print("Extrato CC N %s\n" % self.numero)
        for i in self.operacoes:
            print("%10s %10.2f" % (i[0], i[1]))
        print("\nSaldo: %10.2f" % self.saldo)

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo = 0, limite = 0):
        Conta.__init__(self, clientes, numero, saldo)
        self.saldo = saldo
        self.limite = limite
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE: ", valor])
    def extrato(self):
        saque_disponivel = self.saldo + self.limite
        print("Extrato CC N %s" % self.numero)
        for i in self.operacoes:
            print("%10s %6.2f" % (i[0], i[1]))
        print("\nSaldo: %6.2f \nLimite: %6.2f \nSaldo Disponível para saque: %6.2f" %
              (self.saldo, self.limite, saque_disponivel))
            
                
    
