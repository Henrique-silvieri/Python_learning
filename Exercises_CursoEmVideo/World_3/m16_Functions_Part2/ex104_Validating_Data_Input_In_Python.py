# Create a program that has the function readInt(), which will function similarly to Python's input() function, 
# but providing validation to accept only a numeric value. Ex: n = readInt('Enter a number')

def readInt(prompt):
    isInt = False
    value = 0
    while True:
        number = str(input(prompt))
        if number.isnumeric():
            value = int(number)
            isInt = True
            break
        else:
            print('\033[0;31mERRO, digite um numero inteiro válido.\033[m')
    return value
    

n = readInt('Digite um número inteiro: ')
print(f'O número digitado foi {n}.')
