# Write a program to approve a bank loan for purchasing a house. The program should ask for the value of the house, the buyer's salary, 
# and the number of years over which the loan will be paid. Calculate the monthly installment amount, knowing that it cannot exceed 30% of the buyer's salary;
# otherwise, the loan will be denied.

houseValue = float(input('Qual o valor da casa? R$ '))
salary = float(input('Qual a sua renda mensal? R$ '))
years = int(input('Em quantos anos planeja pagar a casa? '))

installment = houseValue / (years * 12)
maximum_allowed = salary * 0.3

if installment > maximum_allowed:
    requireSalary = installment / 0.3
    print('\nEmpréstimo negado.')
    print(f'A prestação excede 30% do salário. Para esta casa, o salário mínimo recomendado é de R$ {requireSalary:.2f}.')
else:
    print('\nEmpréstimo aprovado. Boa sorte com sua nova casa!')
