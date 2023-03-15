minha_lista = ['Gui', 'João'] # LISTA (list)

minha_tupla = ('Gui', 'João') #TUPLA (tuple)
'''
Serve quando se tem um numero fixo de objeto, pois na tupla, não pode remover e adicionar.
Para substituir tem que ser ela toda.
'''
meu_dicionario = {'nome': 'Guilherme', 'idade': 27}  # DICIONARIO (dict)
'''
funciona como fosse um dicionario, vai ter uma palavra e seu 'significado', vai ter uma chave 
e um valor.
'''
meu_conjunto ={'Gui', 'João'} # CONJUNTO (set)
'''
Parecido com a lista, mas, não pode ter elementos repitidos, se tiver ele ignora e aparece 
apenas um.
'''

print('__________________________________________________________________________')
print('Tuplas:')
minha_tupla = ('João', 'Paulo')
print(f'Tupla {minha_tupla}\n')

if 'Gui' in minha_tupla :
    print('Gui está na tupla') #pode ser feito com lista, dicionario cnjunto
print('__________________________________________________________________________')
print('Dicionário')
print(f'dicionário {meu_dicionario} \n')
print(meu_dicionario['nome']) # para busca mais efeciente.
print('\n')
for chaves in meu_dicionario.keys():
    print(chaves)

print('\n')
meu_dicionario['nome'] = 'João'
print(meu_dicionario)

print('\n')
meu_dicionario['telefone'] = '92987654532'
print(meu_dicionario)

print('__________________________________________________________________________')
print('Conjunto')
print('\n')

print(meu_conjunto)

meu_conjunto.add('Maria')
meu_conjunto.add('Gui')
print(meu_conjunto)

conjunto = set()
