# Write a program that reads a given year and shows whether it is a leap year.

year = int(input('Digite um ano: '))

if year % 4 == 0:
    print(f'{year} é um ano bissexto')
else:
    print(f'{year} não é um ano bissexto')
