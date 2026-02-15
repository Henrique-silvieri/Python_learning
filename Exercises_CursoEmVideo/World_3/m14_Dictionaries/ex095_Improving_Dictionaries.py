# Enhance Challenge 093 so that it works with multiple players, including a system to display detailed performance statistics for each player.

player = {}
goals = []
team = []

while True:
    player.clear()
    player['nome'] = str(input('Qual o nome do jogador? '))
    number_of_matches = int(input(f'Quantas partidas {player["nome"]} jogou? '))
    goals.clear()
    
    for i in range(0, number_of_matches):
        goals.append(int(input(f'Quantos gols {player["nome"]} fez na {i+1}º partida? ')))
    
    player['gols'] = goals[:]
    player['total'] = sum(goals)    
    team.append(player.copy())
    
    continue_ask = str(input('\nDeseja registrar outro jogador? [S/N] ')).lower()[0]
    while continue_ask not in 'SsNn':
        continue_ask = str(input('Valor inválido, deseja registrar outro jogador? [S/N] ')).strip()[0]
    if continue_ask not in 'Ss':
        break

print('-'*46)
print('id         ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('='*46)

for k, v in enumerate(team):
    print(f'{k}' , end='          ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*60)

while True:
    id = int(input('Deseja ver as estatísticas de qual jogador? (999 para sair) '))
    
    if id == 999:
        break
    
    if id >= len(team):
        print(f'ERRO! Não existe nenhum jogador com o id {id} ')
    else:
        print(f' == Levantamento do jogador {team[id]["nome"]} == ')
        for i, g in enumerate(team[id]['gols']):
            print(f'    No jogo {i+1}, {team[id]['nome']} fez {g} gols.')
    print('='*60)
    
print('======= Encerrado ========')
