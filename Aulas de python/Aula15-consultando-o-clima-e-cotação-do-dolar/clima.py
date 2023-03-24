import requests
import json

cidade = input("Escreva a sua cidade :")

requisicao = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=77c10ce1cf3b7daae0b4fb0a49145f0d')

tempo = json.loads(requisicao.text)

print('Condição do tempo: ',tempo['weather'][0]['main'])

