# Create a program that asks for an employee's salary and calculates the amount of their raise. For salaries greater than R$1250, calculate a raise of 10%. For salaries less than or equal to R$1250, the raise is 15%.

salary = float(input('Qual é o salário do funcionário? R$'))

if salary > 1250:
    nem_salary = salary + (salary * 0.1)
else:
    nem_salary = salary + (salary * 0.15)

print(f'Após o aumento o salário é de R${nem_salary:>2f}.')
