# Create a program that reads a student’s name and average grade, also storing their academic status in a dictionary.
# At the end, display the contents of this data structure on the screen.

student = {}
student['nome'] = input("Digite o nome do estudante: ")
grade1 = float(input(f"Digite a nota 1 de {student['nome']}: "))
grade2 = float(input(f"Digite a nota 2 de {student['nome']}: "))
student['média'] = (grade1 + grade2) / 2

if student['média'] >= 7:
    student['status'] = 'Aprovado'
elif 5 <= student['média'] < 7:
    student['status'] = 'Recuperação'
else:
    student['status'] = 'Reprovado'

print('\n--- Dados do Estudante ---')
for k, v in student.items():
    print(f'{k.capitalize()}: {v}')
print('-'*26)