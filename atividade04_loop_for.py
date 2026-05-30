# Autor: Rapha
# Projeto: loop FOR - variaveis de início e fim

numero = int(input('digite o numero para sua tabela:' ))
numero_inicio = int(input('digite o inicio da tabuada:' ))
numero_fim = int(input('digite o fim da tabuada:' ))

# loop FOR
for i in range (numero_inicio, numero_fim + 1):
    print(f'{numero} x {i} = {i * numero}')