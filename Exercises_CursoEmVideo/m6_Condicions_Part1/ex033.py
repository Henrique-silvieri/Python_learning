# Write a program that reads three numbers and displays which one is the largest and which one is the smallest.

number_1 = float(input('Digite um número: '))
number_2 = float(input('Digite outro número: '))
number_3 = float(input('Digite outro número: '))

largest = max(number_1, number_2, number_3)
smallest = min(number_1, number_2, number_3)

if largest == smallest:
    print (f'todos o numero são igual')
else:
    print(f'O maior número é o {largest} e o menor é o {smallest}')
