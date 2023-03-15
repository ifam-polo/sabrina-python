def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp

retorno = soma(12.35, 75.6)
print(retorno)
print('\n')
print('##########################################')
def imprimir_oi():
    print("OI")

imprimir_oi()

print('\n')
print('##########################################')

def tem_sete_letras(argumentos):
    if len(argumentos) == 7:
        return True
    else:
        return False

print(tem_sete_letras("oi pessoal"))
