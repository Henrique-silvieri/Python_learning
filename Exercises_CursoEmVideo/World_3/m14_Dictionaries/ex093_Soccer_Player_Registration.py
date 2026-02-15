# Create a program that manages a soccer player’s performance.
# The program must read the player’s name and the number of matches played.
# Then, it must read the number of goals scored in each match.
# At the end, all this information must be stored in a dictionary, including the total number of goals scored during the championship.

performance = {}
gols = []
total_gols = 0
performance['nome'] = str(input('Qual o nome do jogador? '))
number_of_matches = int(input(f'Quantas partidas {performance["nome"]} jogou? '))
for i in range(number_of_matches):
    gol = int(input(f'Quantos gols {performance["nome"]} fez na {i+1}º partida? '))
    total_gols += gol
    gols.append(gol)
    performance['gols'] = gols
performance['total'] = total_gols

print('='*31)

for k, v in performance.items():
    print(f'O campo {k} tem valor {v}.')

print('='*31)

print(f'O jogador {performance["nome"]} jogou {number_of_matches} partidas.')
for i, v in enumerate(gols):
    print(f'Na partida {i+1}, fez {v} gol(s)')
print(f'No total {performance["nome"]} fez {total_gols}.')