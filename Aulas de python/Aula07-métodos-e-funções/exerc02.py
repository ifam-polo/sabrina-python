'''
EXERCICIO: Escreva uma funcao que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa colecao
faça outra funcao que retorna o menor numero dessa coleçao
'''

def colecao_maior(colecao):
     maior_numero = colecao[0]
     for maior in colecao:
          if maior > maior_numero:
               maior_numero = maior
     return maior_numero

print(colecao_maior([1,2,4,6,1,9,-3]))

def colecao_menor(colecao):
     menor_numero = colecao[0]
     for menor in colecao:
          if menor < menor_numero:
               menor_numero = menor
     return menor_numero

print(colecao_menor([1,2,4,6,1,9,-1,-8]))


