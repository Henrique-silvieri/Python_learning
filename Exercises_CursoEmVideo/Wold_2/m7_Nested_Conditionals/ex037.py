# Write a program that reads an integer from the user and asks them to choose the desired base for conversion:
# -> Enter 1 to convert to binary;
# -> Enter 2 to convert to octal;
# -> Enter 3 to convert to hexadecimal;
# The program should display the result of the conversion according to the user’s choice.

number = int(input('Digite um número inteiro: '))
chosenNumber = int(input('Digite um número para a base de conversão conforme a tabela abaixo:\n'
                    '1 - binário\n'
                    '2 - octal\n'
                    '3 - hexadecimal\n'))

if chosenNumber == 1:
    print(bin(number))
elif chosenNumber == 2:
    print(oct(number))
elif chosenNumber == 3:
    print(hex(number))
else:
    print('Escolha inválida, tente novamente.')
