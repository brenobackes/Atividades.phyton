# Exercício 12 — Divisão segura
# Aluno: Breno Pinheiro
# Objetivo: Ler dois números e se o divisor for zero mostrar erro, caso contrário mostrar o resultado da divisão.

dividendo = int(input('Digite o dividendo: '))
divisor = int(input('Digite o divisor: '))

soma = dividendo / divisor

if divisor == 0:
    print('Erro: não existe divisão por zero')
else:
    print('O resultado da divisão é: ', soma)
