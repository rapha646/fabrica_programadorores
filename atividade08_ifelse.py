# Autor:Rapha
# Projeto:Desvio Condicional


nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso'))
altura = float(input('Digite sua altura '))
imc = peso / (altura** 2)
if imc < 18.5:
    print('abaixo do peso')
else:
    print('pelo normal')