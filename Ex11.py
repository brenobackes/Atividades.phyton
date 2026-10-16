# Exercício 11 — O maior de dois
# Aluno: Breno Pinheiro
# Objetivo: Ler dois números e mostrar qual dos dois é maior.

# Pede dois números ao usuário.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

# Compara os dois números e mostra qual é o maior.
if n1 > n2:
    print('O maior número é: ', n1)
else:
    print('O maior número é: ', n2)