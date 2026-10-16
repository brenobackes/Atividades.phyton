# Exercício 5 — Minutos em horas
# Aluno: Breno Pinheiro
# Objetivo: Receber um valor em minutos do usuário e exibir o valor convertido em horas e minutos.

# Pede um valor ao usuário
minutos = int(input("Digite um valor em minutos: "))

# Calcula o valor em horas e minutos
horas = minutos // 60
minutos_restantes = minutos % 60

# Mostra o valor convertido em horas e minutos
print(horas, "hora(s) e", minutos_restantes, "minuto(s)")