import requests
import json

def requisicao(titulo):
    try:
        req = requests.get(" http://www.omdbapi.com/?apikey=eb931693&t=" + titulo)
        dic = json.loads(req.text) # transforma o conteúdo que está em json para forma de dicionario;
        return dic
    except:
        print('Erro na conexão')
        return None


def printar_detalhes(filmes):
    print('Título: ',filmes['Title'])
    print('Ano: ',filmes['Year'])
    print('Diretor: ',filmes['Director'])
    print('Atores: ', filmes['Actors'])
    print('Nota: ',filmes['imdbRating'])
    print('Premios: ',filmes['Awards'])
    print('Poster:', filmes['Poster'])
    print('')


sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR' :
        SAIR = True
        print('Saindo...')
    else:
        filmes= requisicao(op)
        if filmes['Response'] == 'False' :
            print('Filme não encontrado')
        else:
            printar_detalhes(filmes)
