# The same teacher from the previous exercise wants to randomly select the presentation order of the students' projects. Make a program that reads the names of four students and displays the randomly selected order.

from random import shuffle

first = input('Qual o nome do primeiro aluno? ')
second = input('Qual o nome do segundo aluno? ')
third = input('Qual o nome do terceiro aluno? ')
fourth = input('Qual o nome do quarto aluno? ')
list = [first, second, third, fourth]
shuffle(list)

print(f'A ordem de apresentação será: 1° - {list[0]}\n2° - {list[1]}\n3° - {list[2]}\n4° - {list[3]}')