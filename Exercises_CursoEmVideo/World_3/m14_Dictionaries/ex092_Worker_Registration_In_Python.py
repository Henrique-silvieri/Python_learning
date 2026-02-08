# Create a program that reads a person’s name, year of birth, and work permit number (CTPS), and stores them in a dictionary, 
# replacing the year of birth with the person’s age. If the CTPS number is different from zero, the dictionary must also store the 
# year of hiring and the salary. In addition to the age, calculate and store the age at which the person will retire.

from datetime import datetime

while True:
    dictionary = {}
    
    dictionary['nome'] = name = str(input('Digite o nome: '))
    age_of_birth = int(input('Digite o ano de nascimento: '))
    dictionary['idade'] = datetime.now().year - age_of_birth
    if dictionary['idade'] >= 16:
        dictionary['CTPS'] = int(input('Digite a carteira de trabalho (0 se não tiver): '))
    else:
        print('Idade insuficiente.')
        break
    
    if dictionary['CTPS'] != 0:
        dictionary['contratação'] = int(input('Digite o ano de contratação: '))
        
        if (dictionary['contratação'] - age_of_birth) < 16:
            print('Idade insuficiente')
            del dictionary['contratação']
            break
        else:
            dictionary['salário'] = float(input('Digite o salário: '))
            dictionary['aposentadoria'] =  dictionary['idade'] + ((dictionary['contratação'] + 35) - datetime.now().year)
            break
    else:
        break

print('='*31)
for k, v in dictionary.items():
    print(f'{k} tem o valor {v}')
print('='*31)