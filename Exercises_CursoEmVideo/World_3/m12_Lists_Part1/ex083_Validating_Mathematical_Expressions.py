# Create a program where the user types any expression that uses parentheses.
# Your application must analyze whether the entered expression has the parentheses opened and closed in the correct order.

list = []
list = str(input('Dê a expressão numérica: '))
# print(list.count('('))
if list.count('(') == list.count(')'):
    print('Sua expressão é valida.')
else:
    print('Sua expressão não é valida.')