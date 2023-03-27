import requests
import json
import time
import datetime

while True:
    requisicao = requests.get(
        'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    cotacao = json.loads(requisicao.text)
    print('#### cotação ####', datetime.datetime.now())
    print('Dolar:', cotacao['USDBRL']['high'])
    print('euro:', cotacao['EURBRL']['high'])
    print('BTC:', cotacao['BTCBRL']['high'])
    time.sleep(2)
