lista = [2]
numeros = [3]
num = [5]
primos = [7]

numero = int(input('digite um número: '))
for i in range(2, numero + 1):
    if (i % 2) != 0:
        lista.append(i)

for i in lista:
    if (i % 3) != 0:
        numeros.append(i)

for i in numeros:
    if (i % 5) != 0:
        num.append(i)

for i in num:
    if (i % 7) != 0:
        primos.append(i)
print('numeros primos:', sorted(primos))