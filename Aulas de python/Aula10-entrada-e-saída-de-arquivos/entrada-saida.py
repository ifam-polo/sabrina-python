'''
arquivo = open('arquivo.txt','w')

for i in range(0, 1000):
    arquivo.write("número "+str(i) + "\n")
'''

'''
arquivo = open('arquivo.txt','r')

for linha in arquivo:
    print(linha)
'''
arquivo = open('imagem.jpeg','rb')

print(arquivo.read())







