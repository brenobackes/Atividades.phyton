# Exercício 13 — Senha de acesso
# Aluno: Breno Pinheiro
# Objetivo: Ler a senha correta e permitir o acesso ao sistema.

# Mostra a senha correta e pede ao usuário que digite a senha
senha_correta = 'senai2026'
senha_digitada = input('Digite a senha: ')

if senha_digitada == senha_correta:
    print('Acesso permitido.')
else:
    print('Senha incorreta, acesso negado.')