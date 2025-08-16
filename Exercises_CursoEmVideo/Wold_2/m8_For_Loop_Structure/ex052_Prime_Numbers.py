# Write a program that read a integer and determines whether or not is a prime number

number = int(input('Digite um número inteiro: '))
isPrime = bool

if number <= 1:
    isPrime = False
else:
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break

if isPrime:
    print(f'O número {number} é um número primo')
else:
    print(f'O número {number} não é um numero primo')
