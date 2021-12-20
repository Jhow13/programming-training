from clientes import Cliente
from conta import Conta, ContaEspecial

#Importação e criação de Cliente
joao = Cliente("João da Silva", "777-666")
maria = Cliente("Maria do Bairro", "999-555")
                
#Importação e criação de Conta
conta_1 = Conta("Joao da Silva", 1, "777-666", 200)
conta_2 = Conta("Maria do Bairro", 2, "999-555", 400)
conta_3 = ContaEspecial("José Vieira", 3, 600, 1300)


