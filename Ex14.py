# Exercício 14 — Radar de velocidade
# Aluno: Breno Pinheiro
# Objetivo: Ler a velocidade de um carro e mostrar se ele está acima ou abaixo do limite de velocidade.

# Pede a velocidade do carro.
carro = int(input('Velocidade do carro: '))

# Mostra se o carro estiver acima da velocidade máxima.
if carro > 80:
    print('Multado! Voçê passou', carro - 80, 'km/h do Limite.')
else:
    print('Velocidade dentro do limite. Boa viagem!')