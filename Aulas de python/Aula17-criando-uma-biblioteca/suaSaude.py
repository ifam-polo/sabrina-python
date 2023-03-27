def calcularIMC(peso, altura):
    IMC = peso/(altura**2)
    if IMC > 40:
        return "Obsidade Grau III"
    elif IMC >=35:
        return "Obesidade Grau II"
    elif IMC >= 30:
        return "Obesidade Grau I"
    elif IMC >= 25:
        return "Sobrepeso"
    elif IMC >= 19:
        return "Peso ideal"
    else:
        return "Abaixo do peso ideal"

def iniciarEsporte(esporte):
    if esporte == "corrida":
        return "Inicie correndo 1km por dia"
    elif esporte == "ciclismo":
        return "Inicie pedalando 2km por semana!"
    elif esporte == "academia":
        return "Inicie treinando 3x por semana"
    else:
        return "Esporte não cadastrado!"


def tempoParaAlcancarObjetivo(mes = 0):
    if mes == 0:
        return "Tempo não informado"
    elif mes == 1:
        return "Tempo impossivel"
    elif mes == 2:
        return "Vai depende do seu compromisso"
    elif mes == 3:
        return "Tempo ideal para alcançar o objetivo"
