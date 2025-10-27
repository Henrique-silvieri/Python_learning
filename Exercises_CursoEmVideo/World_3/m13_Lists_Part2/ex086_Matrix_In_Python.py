# Create a program that builds a 3x3 matrix and fills it with values entered by the user through the keyboard.
# In the end, display the matrix on the screen with the proper formatting.

matrix = [[], [], []]

for y in range(3):
    for x in range(3):
        number = int(input(f'Digite um número para por na posição [{y}, {x}]: '))
        matrix[y].append(number)

for i in range(3): 
    for j in range(3):
        print(f'{matrix[i][j]:^5}', end='')
    print()