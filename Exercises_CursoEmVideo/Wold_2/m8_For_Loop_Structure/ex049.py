# Redo exercise 009, displaying the multiplication table of a number chosen by user, but now using a for loop

number = int(input('Qual o número que vc deseja saber a tabuada? '))

for i in range(1, 11):
    print(f'{number} X {i} = {number * i}')
