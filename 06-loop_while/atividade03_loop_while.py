# Autor: Rapha
# Projeto: loop while

numero = int(input('digite a tabua da desejada: '))
inicio = int(input('digite o primeir valor da tabuda '))
fim = int(input('digite o ultimo valor da tabuada '))

while inicio <= fim:
    print(f'{numero} x {inicio} {numero * inicio}')
    inicio = inicio + 1