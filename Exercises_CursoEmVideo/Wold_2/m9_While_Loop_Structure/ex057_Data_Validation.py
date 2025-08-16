# Create a program that reads the sex of a person, but only accepts the values 'M' or 'F'.
# If the input is incorrect, prompt the user again until a valid value is entered.

sex = str(input("Digite seu sexo (M/F): ")).strip().upper()[0]

while sex not in 'MF':
    sex = str(input('Sexo inválido, por vafor digite seu sexo (M/F): ')).strip().upper()[0]
print(f'Sexo {sex} registrado com secesso!')
