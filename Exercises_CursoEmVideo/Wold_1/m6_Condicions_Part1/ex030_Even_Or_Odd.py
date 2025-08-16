# Write a program that reads an integer and displays on the screen whether it is even or odd.

number = int(input('Digite um número inteiro: '))

if number % 2 == 0:
    print(f'O número {number} é par')
else:
    print(f'O número {number} é ímpar')
