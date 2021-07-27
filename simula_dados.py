import random
opcao = 'Digite qualquer tecla para jogar o dado ou '
opcao += 'digite S para sair: '

escolha = ""
while escolha != 's':
    escolha = input(opcao)
    lados = ['lado 1', 'lado 2', 'lado 3', 'lado 4', 'lado 5', 'lado 6']
    sort = random.choice(lados)
    print('O dado caiu em : ', sort)