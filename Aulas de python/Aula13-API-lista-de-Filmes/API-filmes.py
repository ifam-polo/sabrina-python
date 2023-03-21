import requests
import json

req = None
try:
    req = requests.get(" http://www.omdbapi.com/?i=tt3896198&apikey=eb931693")
except:
    print('Erro na conexão')
    exit()


dicionario = json.loads(req.text) # transforma o conteúdo que está em json para forma de dicionario;

print(dicionario)