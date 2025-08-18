# Create a program that reads any number and displays its factorial.

number = int(input('Digite um número: '))
counter = number
factorial = 1
print(f'O valor da fatoral de {number} é: ')
print(f'{number}! = ', end='') 

while counter > 0:
    print(f'{counter}', end='')
    print(' x ' if counter > 1 else ' = ', end='')
    factorial *= counter
    counter -= 1
print(f'{factorial}')

# from math import factorial

# number = int(input('Digite um número para calcular a fatorial: '))
# fact = factorial(number)
# print(f'O valor da fatorial de {number} é {fact},')