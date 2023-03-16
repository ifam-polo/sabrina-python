from veiculo import Veiculo

caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)

print(caminhao_rosa)
print(type(caminhao_rosa))
print('Caminhão')
print("Cor:",caminhao_rosa.cor)
print("Marca:",caminhao_rosa.marca)
print("Tanque:",caminhao_rosa.tanque)
print('\n')

print('Carro')
carro_azul = Veiculo('azul', 4, 'bmw', 30)

print("Cor:",carro_azul.cor)
print("Marca:",carro_azul.marca)
print("Tanque:",carro_azul.tanque)


