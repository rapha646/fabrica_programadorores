# Autor:Rapha
# Projeto:Desvio Condicional


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print('aluno aprovado')
elif media >- 4:
    print('Aluno reprovado')