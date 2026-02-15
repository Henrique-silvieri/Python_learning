# Create a program that has a list called numbers and two functions called draw() and sumEven()
# The first function will draw 5 numbers and place into the list.
# The second function will display the sum of all even numbers drawn by the previous function.

from random import randint
from time import sleep

def draw(list):
    print('Sorteando 5 numeros: ', end='')
    for i in range(0, 5):
        number = randint(1, 10)
        list.append(number)
        print(f'{number} ', end='', flush=True)
        sleep(0.2)
    print('Pronto.')


def sumEven(list):
    sum = 0
    for value in list:
        if value % 2 == 0:
            sum += value
    print(f'A soma dos valores pares da lista acima é {sum}.')



numbers = list()
draw(numbers)
sumEven(numbers)