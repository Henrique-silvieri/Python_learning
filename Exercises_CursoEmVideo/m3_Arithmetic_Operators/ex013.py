# Make a program that reads an employee's salary and shows their new salary with a 15% increase.

salary = float(input('Digite o salario do funcionário (R$): '))
new_salary = salary + (salary * 0.15)
print(f'O novo salário do funcionário, com um aumento de 15% é de R${new_salary:.2f}.')
