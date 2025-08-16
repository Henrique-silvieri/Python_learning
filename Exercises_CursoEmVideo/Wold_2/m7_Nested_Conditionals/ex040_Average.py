# Write a program that reads two grades from a student and calculates their average, showing a message at the end according to the obtained average:
# -> Average below 5.0: FAILED
# -> Average between 5.0 and 6.9: RECOVERY
# -> Average 7.0 or higher: PASSED

grade1 = float(input("Qual a nota 1 do aluno? "))
grade2 = float(input("Qual a nota 2 do aluno? "))
average = (grade1+grade2) / 2

if average < 5:
    print("REPROVADO")
elif 5 <= average < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
