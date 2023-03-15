i = 0

while i<10:
    print(i)
    i = i+1

print('acabou o while : ', i)
print('\n')

lista_frutas = ['marca', 'pera', 'uva', 'abacaxi', 'goiaba', 'lomão', 'laranja']

contador = 0

for fruta in lista_frutas:
    contador+= 1

print('Quantidade de frutas : ', contador)

print('Quantidade de frutas : ', len( lista_frutas))


# Break
numero = 0

while True:
    print(numero)
    if numero == 20:
        break
    numero+=1




