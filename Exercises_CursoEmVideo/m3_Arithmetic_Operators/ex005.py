# Create a program that reads an integer number and displays its successor and predecessor on the screen.

number = int(input('Digite um número inteiro: '))
predecessor = number - 1
sucessor = number + 1
print(f'O número escolhido foi {number}, seu antescessor é {predecessor} e seu antecessor é {sucessor}')
