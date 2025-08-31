# Create a program that displays the multiplication table of multiple numbers, one at a time, for each value entered by the user. The program should be interrupted when the requested number is negative

number = 0

while True:
    number = int(input('\nQual o número que vc deseja saber a tabuada? '))
    
    for i in range(1, 11):
        print(f'{number} X {i} = {number * i}')
    
    if number < 0:
        break
print('\nFim do programa.')