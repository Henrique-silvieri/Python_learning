# Improve the previous challenge by showing at the end:
# A) The sum of all even values entered.
# B) The sum of the values in the third column.
# C) The largest value in the second row.

matrix = [[], [], []]
evens_sum = sum_third_column = max_second_row =  0

for y in range(3):
    for x in range(3):
        number = int(input(f'Digite um número para por na posição [{y}, {x}]: '))
        matrix[y].append(number)
        
        if number % 2 == 0:
            evens_sum+= number       
              
sum_third_column = matrix[0][2] + matrix[1][2] + matrix[2][2]
max_second_row = max(matrix[1])

for i in range(3): 
    for j in range(3):
        print(f'{matrix[i][j]:^5}', end='')
    print()

print(f'\nSoma dos números pares: {evens_sum}.')
print(f'Soma dos valores da terceira coluna: {sum_third_column}.')
print(f'O maior valor da segunda linha: {max_second_row}.')