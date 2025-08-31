# Create a program that reads two values and displays a menu on the screen:
# [1] Add
# [2] Multiply
# [3] Determine the greater value
# [4] Enter new numbers
# [5] Exit the program
# Your program should perform the operation requested in each case.

navigation = 0
number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))
menu = '''
O que deseja fazer?
[1] Adição
[2] Multipliplicação
[3] Determinar o mair valor
[4] Adicionar novos valores
[5] Sair do programa \n
'''

while navigation != 5:
    navigation = int(input(menu))
    
    if navigation == 1:
        sum = number1 + number2
        print(f'\nO valor da soma dos números {number1} e {number2} é {sum}.')
    
    elif navigation == 2:
        multiply = number1 * number2
        print(f'\nO valor da multiplicação dos números {number1} e {number2} é {multiply}.')
    
    elif navigation == 3:
        if number1 > number2:
            print(f'\nO maior valor entre {number1} e {number2} é {number1}.')
        elif number1 < number2:
            high = number2
            print(f'\nO maior número entre {number1} e {number2} é {number2}.')
        else:
            print('\nOs números são iguais.')
    
    elif navigation == 4:
        number1 = int(input('\nDigite um número: '))
        number2 = int(input('\nDigite outro número: '))
    
    elif navigation == 5:
        print('\nPrograma finalizado.\n')
        break
    
    else:
        print('Escolha inválida. Digite um valor de 1 a 5.')
