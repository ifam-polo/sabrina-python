import json
import requests


def lista_filmes(titulo):
    lista = []
    for i in range(1,101):
        try:
            print('Pesquisando em página:', i)
            req = requests.get('http://www.omdbapi.com/?apikey=eb931693&s=' + titulo + '&type=movie&page='+ str(i))
            resposta = json.loads(req.text)
            if resposta ['Response'] == 'False':
                print('Fim das páginas')
                break
            else:
                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    string = tit + '(' + ano + ')'
                    lista.append(string)
        except:
            print('Conexão falhou')

    return lista


sair = False
while not sair:
    op = input('Pesquise por um filme ou digite SAIR: ')
    if op == "SAIR":
        sair = True
    else:
        lista_de_filmes = lista_filmes(op)
        print('Filmes encontrados', len(lista_de_filmes))
        for filme in lista_de_filmes:
            print(filme)



