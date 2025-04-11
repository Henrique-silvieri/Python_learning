# A teacher wants to randomly select a student to clean the board. Make a program that helps with this task by reading their names and displaying the chosen name.

from random import choice

first = input('Qual o nome do primeiro aluno? ')
second = input('Qual o nome do segundo aluno? ')
third = input('Qual o nome do terceiro aluno? ')
fourth = input('Qual o nome do quarto aluno? ')
list = [first, second, third, fourth]

print(f'O(a) escolhido para apagar a lousa foi o(a) {choice(list)}')
