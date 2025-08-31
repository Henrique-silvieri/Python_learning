# Write a program that reads two integer numbers and compares them, displaying one of the following messages:
# -> "The first value is greater"
# -> "The second value is greater"
# -> "There is no greater value, both are equal"

number1 = float(input('Digite um número: '))
number2 = float(input('Digite outro número: '))

if number1 > number2:
    print('O primeiro número é maior que o segundo')
elif number1 < number2:
    print('O segundo número é maior que o primeiro')
else:
    print('Ambos valores são iguais')
