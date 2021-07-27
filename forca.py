import random

# Aqui abro o arquivo com as palavras guardadas
arquivo = open('palavras.txt', 'r')
palavras = arquivo.readlines()
# Aqui sorteio uma palavra
palavra = random.choices(palavras)
# Aqui retiro o espaço vazio depois da palavra
for nova in palavra:
    nova = nova.strip()
# Aqui utilizo o len para contar a quantidade de letras
contador = len(nova)
# Aqui fecho o arquivo
arquivo.close()

# print('aqui é depois do sorteio', nova)
res = list(nova)
# print('aqui é depois de converter em lista', res)

contp = len(nova)

certa = []

errada = []

v = 0

resu = ['_', '_', '_', '_', '_', '_', '_']

def forca(forca):
    if v == 0:
        print(' +---+')
        print(' |   |')
        print('     |')
        print('     |')
        print('     |')
        print('     |')

    elif v == 1:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('     |')
        print('     |')
        print('     |')

    elif v == 2:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print(' |   |')
        print('     |')
        print('     |')

    elif v == 3:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|   |')
        print('     |')
        print('     |')

    elif v == 4:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('     |')
        print('     |')

    elif v == 5:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('/    |')
        print('     |')

    elif v == 6:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('/ \  |')
        print('     |')

class bcolors:
    OK = '\033[92m' #GREEN
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

while (v < contp) or (resu == res) == True:

    print('')
    print('')
    print('')
    print('>>>>>>>>>>>>>> Hangman <<<<<<<<<<<<<')
    print('')
    print(forca(0))
    print('=========')
    print('')
    print('Palavra: ', ''.join(map(str, resu)))
    print('')
    print('Letras Erradas: ')
    erro = list(set(errada))

    for er in erro:
        print(f"{bcolors.FAIL}" +er + f"{bcolors.RESET}")
    print('')

    v = len(erro)

    print('Letras Corretas: ')

    certo = list(set(certa))
    for ce in certo:
        print(f"{bcolors.OK}" + ce + f"{bcolors.RESET}")
    print('')

    letra = input("Digite uma letra: ")
    print('')
    print(v == 6)

    if (letra == res[0]) and (letra == res[2]) and (letra == res[4]) and (letra == res[6]):

        resu[6] = letra
        resu[4] = letra
        resu[2] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[0]) and (letra == res[2]) and (letra == res[3]):

        resu[3] = letra
        resu[2] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[0]) and (letra == res[2]) and (letra == res[4]):

        resu[4] = letra
        resu[2] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[0]) and (letra == res[2]) and (letra == res[6]):

        resu[6] = letra
        resu[2] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[0]) and (letra == res[3]) and (letra == res[6]):

        resu[6] = letra
        resu[3] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[0]) and (letra == res[4]) and (letra == res[6]):

        resu[6] = letra
        resu[4] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[1]) and (letra == res[2]) and (letra == res[6]):

        resu[6] = letra
        resu[2] = letra
        resu[1] = letra
        certa.append(letra)

    elif (letra == res[1]) and (letra == res[3]) and (letra == res[6]):

        resu[6] = letra
        resu[3] = letra
        resu[1] = letra
        certa.append(letra)

    elif (letra == res[1]) and (letra == res[3]) and (letra == res[5]):

        resu[5] = letra
        resu[3] = letra
        resu[1] = letra
        certa.append(letra)

    elif (letra == res[1]) and (letra == res[4]) and (letra == res[6]):

        resu[6] = letra
        resu[4] = letra
        resu[1] = letra
        certa.append(letra)

    elif (letra == res[2]) and (letra == res[4]) and (letra == res[6]):

        resu[6] = letra
        resu[4] = letra
        resu[2] = letra
        certa.append(letra)

    elif (letra == res[0]) and (letra == res[5]):

        resu[5] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[0]) and (letra == res[6]):

        resu[6] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[0]) and (letra == res[3]):

        resu[3] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[0]) and (letra == res[4]):

        resu[4] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[0]) and (letra == res[2]):

        resu[2] = letra
        resu[0] = letra
        certa.append(letra)

    elif (letra == res[1]) and (letra == res[6]):

        resu[6] = letra
        resu[1] = letra
        certa.append(letra)

    elif (letra == res[1]) and (letra == res[3]):

        resu[3] = letra
        resu[1] = letra
        certa.append(letra)

    elif (letra == res[1]) and (letra == res[5]):

        resu[5] = letra
        resu[1] = letra
        certa.append(letra)

    elif (letra == res[1]) and (letra == res[4]):

        resu[4] = letra
        resu[1] = letra
        certa.append(letra)

    elif (letra == res[1]) and (letra == res[2]):

        resu[2] = letra
        resu[1] = letra
        certa.append(letra)

    elif (letra == res[2]) and (letra == res[6]):

        resu[6] = letra
        resu[2] = letra
        certa.append(letra)

    elif (letra == res[2]) and (letra == res[5]):

        resu[5] = letra
        resu[2] = letra
        certa.append(letra)

    elif (letra == res[2]) and (letra == res[4]):

        resu[4] = letra
        resu[2] = letra
        certa.append(letra)

    elif (letra == res[2]) and (letra == res[3]):

        resu[3] = letra
        resu[2] = letra
        certa.append(letra)

    elif (letra == res[3]) and (letra == res[6]):

        resu[6] = letra
        resu[3] = letra
        certa.append(letra)

    elif (letra == res[3]) and (letra == res[5]):

        resu[5] = letra
        resu[3] = letra
        certa.append(letra)

    elif (letra == res[4]) and (letra == res[6]):

        resu[6] = letra
        resu[4] = letra
        certa.append(letra)

    elif (letra == res[3]) and (letra == res[4]):

        resu[4] = letra
        resu[3] = letra
        certa.append(letra)

    elif (letra == res[4]) and (letra == res[5]):

        resu[4] = letra
        resu[5] = letra
        certa.append(letra)

    elif (letra == res[0]):

        resu[0] = letra
        certa.append(letra)

    elif (letra == res[1]):

        resu[1] = letra
        certa.append(letra)

    elif (letra == res[2]):

        resu[2] = letra
        certa.append(letra)

    elif (letra == res[3]):

        resu[3] = letra
        certa.append(letra)

    elif (letra == res[4]):

        resu[4] = letra
        certa.append(letra)

    elif (letra == res[5]):

        resu[5] = letra
        certa.append(letra)

    elif (letra == res[6]):

        resu[6] = letra
        certa.append(letra)

    elif (letra != res[0]) or (letra != res[1]) or (letra != res[2]) or (letra != res[3]) or (letra != res[4]) or (letra != res[5]) or (letra != res[6]):
        errada.append(letra)

    if (v == 6) == True:
        print('')
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('/ \  |')
        print('     |')
        print('=========')
        print('Você errou sete letras : ')
        for er in erro:
            print(f"{bcolors.FAIL}" +er + f"{bcolors.RESET}")

        print(f'{bcolors.FAIL}' + errada[-1] + f'{bcolors.RESET}')
        print('')
        print('A palavra correta era: ', nova)

        break

    if (resu == res) == True:
        print('')
        print(forca(0))
        print('=========')
        print('Palavra: ', ''.join(map(str, resu)))
        print('')
        print('Parabéns você acertou a palavra: ', nova)
        print('')
        print('Letras Erradas: ')
        for er in erro:
            print(f"{bcolors.FAIL}" +er + f"{bcolors.RESET}")
        print('')
        print('Letras Corretas: ')
        for ce in certo:
            print(f"{bcolors.OK}" + ce + f"{bcolors.RESET}")

        break

    v = len(erro)
