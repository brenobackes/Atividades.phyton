# Exercício 6 — Compra na cantina
# Aluno: Breno Pinheiro
# Objetivo: Receber o valor de uma compra na cantina do colégio e exibir a quantidade e o valor pago.

# Pede o preço do produto, quantidade e o valor pago
preco = float(input('Digite o preço do produto comprado: '))
quantidade = int(input('Digite a quantidade de produtos da compra: '))
valor_pago = float(input('Digite quantos voçê pagou: '))

# Calcula o total da compra e o troco
total_compra = preco * quantidade
total =  valor_pago - total_compra

# Mostra o total e o troco
print('Valor total da compra: ', total_compra)
print('Troco: ', total)