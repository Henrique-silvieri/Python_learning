# Create a program that reads the length of 3 segments and tells the user whether they can or cannot form a triangle.

segment1 = float(input('Digite o comprimento da primeira reta: '))
segment2 = float(input('Digite o comprimento da segunda reta: '))
segment3 = float(input('Digite o comprimento da terceira reta: '))

if segment1 + segment2 >= segment3 and segment1 + segment3 >= segment2 and segment2 + segment3 >= segment1:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
