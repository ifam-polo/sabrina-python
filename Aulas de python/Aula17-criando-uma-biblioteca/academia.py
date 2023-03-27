import suaSaude

grau_obesidade = suaSaude.calcularIMC(float(input("Digite seu peso: ")),
                                      float(input("Digite sua altura: ")))

print("Grau de obesidade: ",grau_obesidade)

ficha_treino = suaSaude.iniciarEsporte(input("Digite o esporte que irá iniciar : ").lower())
print("Ficha do seu treino: ", ficha_treino)

objetivo = suaSaude.tempoParaAlcancarObjetivo(int(input("Com quantos meses deseja alcançar seu objetivo: ")))

print(objetivo)