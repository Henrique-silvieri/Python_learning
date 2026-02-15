# Create a program that has a function called playerRecord(), which receives two optional parameters: 
# a player's name and how many goals they scored. The program must be able to show the player's record even if some data has not been entered correctly

def playerRecord(name='', goal=''):
    if name == '':
        name = '<DESCONHECIDO>'
    if goal == '':
        goal = '0'
    return f'O jogador {name} fez {goal} gol(s)'


playerName = str(input('Digite o nome do jogador: ')).capitalize().strip()
goals = str(input(f'Digite a quantidade de gol(s) feitos: ')).strip()
print(playerRecord(playerName, goals))
