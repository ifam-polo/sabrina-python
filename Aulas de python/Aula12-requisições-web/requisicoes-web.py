import requests
'''
requisicao = requests.get('http://www2.ifam.edu.br')
print(requisicao)
print(type(requisicao))
print(requisicao.status_code)
print(requisicao.text)
'''


cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com',
             'cf_ipcountry':'US'}

meus_cookies = {'Ultimas-visita': '10-10-2020'}

dados = {'username': 'guigui',
         'password': 'guigui123'}

texto = None
try:
    requisicao = requests.get('https://putsreq.com/a5G6bby5T6eJFZaanqDa',
                               headers=cabecalho,
                               cookies=meus_cookies,
                               data=dados)
    texto = requisicao.text
except Exception as e:
    print("Requisição deu erro :", e)

print(texto)

