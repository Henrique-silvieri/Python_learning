# Create a tuple filled with the top 20 teams from the Brazilian Football Championship Table, in order of ranking. Then display:
# A) Only the top 5 teams.
# B) The last 4 teams in the table.
# C) A list of the teams in alphabetical order.
# D) The position in the table of the São Paulo team.

ranking = ('Flamengo', 
'Cruzeiro', 
'Palmeiras', 
'Bahia', 
'Botafogo', 
'Mirassol', 
'São Paulo', 
'Bragantino', 
'Fluminense', 
'Ceará SC',
'Corinthians', 
'Grêmio',
'Atlético-MG',
'Internacional',
'Santos',
'Juventude',
'Vasco da Gama',
'EC Vitória',
'Fortaleza',
'Sport Recife')

print('O top 5 times do Brasileirão é: ')
for pos, team in enumerate(ranking[:5]):
    print(f'{pos+1}º - {team}')

print('\nOs últimos 4 times da tabela são: ')
for pos, team in enumerate(ranking[-4:]):
    print(f'{pos+17}º - {team}')

print('\nOs times do brasileirão em ordem alfabética é: ')
for time in sorted(ranking):
    print(f'{time}')

print(f'\nA posição do São Paulo na tabela é a {ranking.index("São Paulo") + 1}ª posição')