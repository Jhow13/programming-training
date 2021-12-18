from cidades import Cidade
from estados import Estado

#Criação dos objetos e importação de Cidades
cidade_1 = Cidade("Ribeirão Pires", 3000)
cidade_2 = Cidade("Mauá", 5000)
cidade_3 = Cidade("Juiz de Fora", 4500)
ciade_4 = Cidade("Copacabana", 12600)
cidade_5 = Cidade("Belf Roxo", 2000)

#Criação dos objetos  e importação de Estados
estado_1 = Estado('São Paulo', 'SP')
estado_2 = Estado('Minas Gerais', 'MG')
estado_3 = Estado('Rio de Janeiro', 'RJ')

#Teste dos objetos
estado_1.resumo()
estado_1.inseri_cidade('Ribeirão Pires', 12500)
estado_1.inseri_cidade('Maua', 30265)
estado_1.inseri_cidade('Susano', 11598)
estado_1.lista_cidades()
