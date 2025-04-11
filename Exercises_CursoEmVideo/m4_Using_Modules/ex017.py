# Make a program that reads the length of the opposite leg and the adjacent leg of a right-angled triangle. Calculate and display the length of the hypotenuse.

from math import hypot
opposite_leg = float(input('Qual é o cateto oposto do triângulo? '))
adjacent_leg = float(input('Qual é o cateto adjacente do triângulo? '))
hypotenuse = hypot(opposite_leg, adjacent_leg)

print(f'O valor da hipotenusa deste triângulo vale: {hypotenuse:.2f}')
