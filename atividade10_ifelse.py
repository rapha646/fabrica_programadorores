# Autor:Rapha
# Projeto:Desvio Condicional

# criaçaõ de variaveis
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso kg: "))
altura = float(input("Digite sua altura em metros: ")) 

# calculo do imc
imc = peso / (altura ** 2)

if imc <= 18.5:
   print("abaixo do peso")
elif imc <= 18.5:
   print("peso normal")
elif imc <= 25:
   print("sobrepeso")
elif imc <= 30: 
   print("obesidade grau I")
elif imc >=35:
   print("obesidade grau II")
else:
    print('obesidade grau III')


