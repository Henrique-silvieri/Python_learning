# create a algorithm that reads a number and display its double, triple and square root

from math import sqrt

number = float(input('Digite  um número: '))
double = number * 2
triple = number * 3
square_root = sqrt(number)
print(f'O número digitado foi {number}\nSeu dobro é {double}\nSeu triplo é {triple}\nSua raiz quadrada é {square_root:.2f}')
