'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas que
serao convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e
colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista
'''

print('Programinha de controle de festinha 1.0')
print('###########################################')

numero_do_convidados = int(input('Coloque o numero de convidados : \n'))
lista_de_convidados =[]
i=1
while i <= numero_do_convidados :
        nome_do_convidado = input('Coloque o nome do convidado #'+ str(i) +' : ')
        lista_de_convidados.append(nome_do_convidado)
        i += 1

print(f'Serão {numero_do_convidados} convidados')
print('Lista de convidados: ')
for convidado in lista_de_convidados:
    print(convidado)
