# Create a program where four players roll the dice and get random results. Store these results in a dictionary.
# At the end, sort the dictionary, knowing that the winner is the one who rolled the highest number on the dice.

from random import randint
from time import sleep
from operator import itemgetter

players = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
    }

ranking = ()

print('\n--- Resultados das rolagens ---')

for player, roll in players.items():
    print(f'{player} rolou um {roll}')
    sleep(1)

print('-'*31)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)

print('=== Ranking dos Jogadores ===')

for i, value in enumerate(ranking):
    print(f'{i+1}º lugar: {value[0]} com {value[1]}')
    sleep(1)

print('='*29)