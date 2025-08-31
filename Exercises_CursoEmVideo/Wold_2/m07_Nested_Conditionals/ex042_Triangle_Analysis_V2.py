# Redo exercise 035 about triangles, adding the feature to display which type of triangle will be formed:
# -> Equilateral: all sides are equal
# -> Isosceles: two sides are equal
# -> Scalene: all sides are different

segment1 = float(input('Digite o comprimento da primeira reta: '))
segment2 = float(input('Digite o comprimento da segunda reta: '))
segment3 = float(input('Digite o comprimento da terceira reta: '))


if segment1 + segment2 >= segment3 and segment1 + segment3 >= segment2 and segment2 + segment3 >= segment1:
    if segment1 == segment2 == segment3:
        triangleType = 'equilátero'
    elif segment1 == segment2 != segment3 or segment1 == segment3 != segment2 or segment2 == segment3 != segment1:
        triangleType = 'isósceles'
    else:
        triangleType = 'escaleno'
        
    print(f'É possível formar um triângulo, o tipo do triangulo formado é: {triangleType}.')

else:
    print('Não é possível formar um triângulo.')

