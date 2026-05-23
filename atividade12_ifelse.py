# Autor:Rapha
# Projeto:Desvio Condicional


nome = input('Digite seu nome: ')
telefone = input('Digite seu telefone')
cidade = input('Digite sua cidade ')
salario = float(input('digite seu salrio: '))
if salario >=1000:
    print('voce possui uma renda boa')
elif salario >= 500:
    print('voce possui uma renda baixa')
else:
    print('voce possui uma renda muito baixa')