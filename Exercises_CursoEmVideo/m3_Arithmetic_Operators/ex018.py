# Make a program that reads any angle and displays on the screen the values of the sine, cosine, and tangent of this angle.

from math import radians, sin, cos, tan
angle = float(input('Digite o ângulo que você deseja: '))
sin, cos, tan= sin(radians(angle)), cos(radians(angle)), tan(radians(angle))

print(f'O seno vale: {sin:.2f}\nO cosseno vale: {cos:.2f}\nA tangente vale: {tan:.2f}')
