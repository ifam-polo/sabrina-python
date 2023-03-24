import re
import requests

requisicao = requests.get('https://fpftech.com/contato/fale-conosco')

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text) # RAW String '. ou \w (os espaços brancos não considera)' para ignorar a caracter seguinte

if padrao:
    print(padrao)
else:
    print("Padrão não encontrado")




