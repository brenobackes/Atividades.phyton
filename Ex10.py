# Exercício 10 — Aprovado ou reprovado
# Aluno: Breno Pinheiro
# Objetivo: Ler a nota de um aluno e informar se ele foi aprovado ou reprovado.

# Pede as notas do aluno.
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

# Soma e faz a média das notas.
soma = n1 + n2 
media = soma / 2
# Mostra a Media das notas.
print('Essa foi sua média: ', media)

# Verifica se a media é maior ou menor que 7.
if media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')