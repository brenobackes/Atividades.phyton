# Exercício 9 — Par ou ímpar
# Aluno: Breno Pinheiro
# Objetivo: Ler um número e identificar se ele é impar ou par.

# Pede um número ao usúario.
n = int(input('Digite um número: '))

# Divide o número por 2 e verifica se o resto foi 0.
if n % 2 == 0:
    print('O número é par!')
else:
    print('O número é ímpar!')