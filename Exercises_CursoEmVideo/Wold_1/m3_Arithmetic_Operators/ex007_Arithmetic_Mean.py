# Develop a program that reads two grades from a student and displays their average.

grade_1 = float(input('Qual a primeira nota do aluno? '))
grade_2 = float(input('Qual a segunda nota do aluno? '))
avarage = (grade_1 + grade_2) / 2
print(f'A média do  aluno é de {avarage:.2f}')
