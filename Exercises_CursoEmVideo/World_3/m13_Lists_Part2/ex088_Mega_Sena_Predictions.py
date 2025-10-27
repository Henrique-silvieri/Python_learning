# Create a program that helps a Mega Sena player generate betting suggestions.
# The program should ask how many games will be generated, then draw 6 random numbers between 1 and 60 for each game, 
# storing everything inside a composite list.

import random, time

bet = []
games = []
number_of_games =int(input('Quando jogos você quer que sejam gerados? '))

print()
print('~-'*30)
for i in range(number_of_games):
    while len(bet) < 6:
        numbers = random.randint(1, 60)
        if numbers not in bet:
            bet.append(numbers)
    bet.sort()
    games.append(bet[:])
    bet.clear()
    print(games[i])
    time.sleep(1)
print('~-'*30)