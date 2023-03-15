# Faça um programa que leia a quantidade de pessoas que serao convidadas para uma festa
# Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados.
# após isso irá imprimir todos os nomes da lista.

lista_nome = []
quant = int(input('Informe a quantidade de convidados : \n'))

for i in range(quant):
    nome = input(f'Nome do convidado {i+1} : ')
    lista_nome.append(nome)

print('Lista de convidados: ')
for convidados in lista_nome:
    print(convidados)




