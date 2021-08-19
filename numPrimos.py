lista = [2]
lista1 = [3]
lista2 = [5]
lista3 = [7]
print('Números Primos')
# Entrada de numero para consulta
numero = int(input('Digite um número: '))
for i in range(2, numero + 1):
    if (i % 2) != 0:
        lista.append(i)

for i in lista:
    if (i % 3) != 0:
        lista1.append(i)

for i in lista1:
    if (i % 5) != 0:
        lista2.append(i)

for i in lista2:
    if (i % 7) != 0:
        lista3.append(i)

if numero in lista3 and numero == 2:
    print('O número', numero, 'é primo e está na lista', lista)

elif numero in lista3 and numero == 3:
    print('O número', numero, 'é primo e está na lista', sorted(lista1))

elif numero == 1:
    print('O número', numero, 'não é primo')

elif numero == 4:
    print('O número', numero, 'não é primo nesta lista', sorted(lista1))

elif numero in lista3 and numero == 5:
    print('O número', numero, 'é primo e está na lista', sorted(lista2))

elif numero == 6:
    print('O número', numero, 'não é primo nesta lista', sorted(lista2))

elif numero in lista3 and numero == 7:
    print('O número', numero, 'é primo e está na lista', sorted(lista3))

elif numero in lista3:
    print('O número', numero, 'é primo nesta lista', sorted(lista3))

else:
    print('O número', numero, 'não é primo nesta lista', sorted(lista3))