peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / altura**2

if imc < 17:
    print('Muito abaixo do peso {:.2f}'.format(imc))

elif imc >= 17 and imc <= 18.49:
    print('Abaixo do peso {:.2f}'.format(imc))

elif imc >= 18.5 and imc <= 24.99:
    print('Peso normal {:.2f}'.format(imc))

elif imc >= 25 and imc <= 29.99:
    print('Acima do peso {:.2f}'.format(imc))

elif imc >= 30 and imc <= 34.99:
    print('Obesidade I {:.2f}'.format(imc))

elif imc >= 35 and imc <= 39.99:
    print('Obesidade II {:.2f}'.format(imc))

elif imc > 40:
    print('OBESIDADE III MORBIDA {:.2f}'.format(imc))