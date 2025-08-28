# Create a program that plays “Even or Odd” with the computer. The game should only be interrupted when the player loses, displaying the total number of consecutive victories achieved by the player at the end of the game.
from random import randint

number = result = total = evenorodd = victoryStreak = 0

print('Vamos jogar par ou impar!', end=' ')

while True:
    evenorodd = int(input('Você escolhe par ou impar? \n[1] - impar \n[2] - par \n'))
    number = int(input('[Qual número você quer escolher?] '))
    enemyNumber = randint(0, 5)

    total = number + enemyNumber
    
    if evenorodd == 1:
        if total % 2 == 0:
            result = 0
        else:
            result = 1
    else:
        if total % 2 == 0:
            result = 1
        else:
            result = 0
    
    if result == 0:
        break
    else:
        victoryStreak += 1
        print(f'Eu escolhi {enemyNumber}, {total} é {'par' if total % 2 == 0 else 'impar'}, você ganhou!')

print(f"Eu escolhi {enemyNumber}, {total} é {'par' if total % 2 == 0 else 'impar'}, você perdeu!")
print(f'Sua sequência de vitorias foi de {victoryStreak}!')

# The variable result holds either 0 or 1, indicating victory or defeat.