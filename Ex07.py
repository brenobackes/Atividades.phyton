# Exercício 7 — Maior ou menor de idade
# Aluno: Breno Pinheiro
# Objetivo: Ler a idade de uma pessoa e mostrar se ela é de maior ou menor.

# Lê a idade que o usúario digitou.
idade = int(input('Digite sua idade: '))

# Verifica se a idade digitada é maior ou menor que 18.
if idade >= 18:
    print('Maior de idade!')
else:
    print('Menor de idade!')