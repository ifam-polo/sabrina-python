import re
import requests

requisicao = requests.get('https://fpftech.com/')

padrao = re.findall(r'/[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text) # RAW String '. ou \w (os espaços brancos não considera)' para ignorar a caracter seguinte


print(padrao)


