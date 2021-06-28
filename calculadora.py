print('')
print('********************* Python Calculadora *********************')
print('')
print('Selecione o númenro da operação desejada: ')
print('')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('')

opc = int(input('Digite sua opção (1/2/3/4): '))

print('')
num = int(input('Digite um número: '))
print('')
num1 = int(input('Digite o segundo número: '))
print('')

if opc == 1:
    soma = num + num1
    print(num, '+', num1, '=', soma)

if opc == 2:
    soma = num - num1
    print(num, '-', num1, '=', soma)

if opc == 3:
    soma = num * num1
    print(num, '*', num1, '=', soma)

if opc == 4:
    soma = num / num1
    print(num, '/', num1, '=', soma)

if opc != 1 or opc != 2 or opc != 3 or opc != 4:
    print('Opção Inválida')