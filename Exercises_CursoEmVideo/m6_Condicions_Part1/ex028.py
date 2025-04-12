# Write a program that makes the computer "think" of a random integer number between 0 and 5 and asks the user to try to guess the number chosen by the computer. The program must display on the screen whether the user won or lost.

from random import randint

guess = int(input('Adivinhe o numero que eu estou pensando de 1 a 5: '))
number = randint(1, 5)

if guess == number:
    print('PARABENS, VOCÊ ACERTOU!!!')
else:
    print('Errado... mais sorte da próxima vez!')
