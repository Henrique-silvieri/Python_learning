# # Write a program that reads any integer number n and displays on the screen the first n elements of a Fibonacci sequence.

n = int(input('Quantos termos você quer mostrar? '))
term1 = 0
term2 = 1
count = 0

print(f'Sequência de Fibonacci:')

while count < n:
    if count == 0:
        print(f'{term1}', end='')
    elif count == 1:
        print(f' - {term2}', end='')
    else:
        term3 = term1 + term2
        print(f' - {term3}', end='')
        term1 = term2
        term2 = term3
    count += 1
