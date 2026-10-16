# Exercício 2 — Operações básicas
# Aluno: Breno Pinheiro
# Objetivo: Receber dois números do usuário e exibir a soma, subtração e multiplicação desses números.

# Pede dois números do usuário
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

# Soma, subtração e multiplicação dos números
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2

# Mostra os resultados das contas
print("A soma de ", n1 ,"+", n2 ,"é", soma)
print("A subtração de ", n1 ,"-", n2 ,"é", subtracao)
print("A multiplicação de ", n1 ,"*", n2 ,"é", multiplicacao)