# Improve the game from ex028, where the computer will "think" of a number between 0 and 10.
# Now, however, the player will try to guess until they get it right, and at the end, the program should display how many attempts were needed to win.

from random import randint

guess = int(input('Pensei em um número de 0 a 10, tente adivinhar: '))
number = randint(0, 10)
attemps = 0

if guess == number:
    print('UAU! Parebéns, você acertou de primeira!')
else: 
    while guess != number:
        guess = int(input('Você errou! Digite um número de 0 a 10: '))
        attemps+=1
        number = randint(0, 10)
    
    print(f'Parabéns!!! Você acertou! houve um total de {attemps+1} tentativas.')
