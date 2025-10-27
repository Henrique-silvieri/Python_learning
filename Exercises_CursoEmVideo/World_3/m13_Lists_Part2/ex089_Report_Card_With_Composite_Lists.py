# Create a program that reads the name and two grades of several students and stores all the information in a composite list.
# At the end, display a report containing the average grade of each student, and allow the user to view the individual grades of any selected 
# student.

students = []

while True:
    name = str(input('Nome: '))
    grade1 = float(input('Nota 1: '))
    grade2 = float(input('Nota 2: '))
    average = (grade1 + grade2) / 2
    students.append([name, [grade1, grade2], average])
    
    continue_answer = ' '
    while continue_answer not in 'SN':
        continue_answer = str(input('Deseja cadastrar outro aluno (S/N)? ')).strip().upper()[0]

    if continue_answer == 'N':
        break
    
print('-'*25)
print(f'{"No.":<5}{"No.":<10}{"Média":>10.1}')
print('-'*25)
for i, a in enumerate(students):
    print(f'{i:<5}{a[0]:<10}{a[2]:>10}')
print('-'*25)

print()
while id != 999:
    print('--'*30)
    
    id = int(input('\nDeseja ver as notas de qual estudante?(999 para sair) '))
    
    if id == 999:
        break
    if id <= len(students) - 1:
        print(f'As notas de {students[id][0]} são {students[id][1]}')