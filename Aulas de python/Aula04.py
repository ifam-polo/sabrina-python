#Strigs  e Lista

frase = 'Oi, Tudo bem?'
lista_nomes =['Joao', 'Maria', 'Guilherme', 'Diego']
lista_nomes.append('Geralda')
lista_nomes.append('Lorena')
lista_nomes.remove('Joao')
lista_nomes.insert(1, 'Creosvaldo') # acrescenta
lista_nomes[0] = 'Robervanio' #susbstitui
contador_joao = lista_nomes.count('Joao') #conta quantos tem


print(contador_joao)
print(lista_nomes)
print(frase[0:5])
print(frase[0:13:1])
print(lista_nomes[0:2])
print(lista_nomes[-1]) # Os números negativos: ultimo  elemento da lista, e tbm anda de trás pra frente.
print(lista_nomes[-1:-4:-1])
print(frase[::-1]) # Inverte tudo;

print(frase.lower()) #para minúsculo
print(frase)
frase_separada = frase.split(',')
print(frase_separada)




