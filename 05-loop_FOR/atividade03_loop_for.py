# Autor: Rapha
# Projeto: Tabuada com loop FOR

numero = int(input('digite o numero para sua tabela:' ))

for i in range (1,11):
    print(f'{numero} x {i} = {i * numero}')