# Develop a logic that reads a person's weight and height, calculates their BMI, and displays their status according to the table below:
# -> Below 18.5: Underweight
# -> Between 18.5 and 25: Ideal weight
# -> From 25 to 30: Overweight
# -> From 30 to 40: Obesity
# -> Above 40: Morbid obesity

weight = float(input('Qual é o seu peso?(Kg) '))
height = float(input('Qual a sua altura?(m) '))
imc = weight / height^2

if imc < 18.5:
    status = 'abaixo de seu peso ideal'
elif imc >= 18.5 and imc < 25:
    status = 'em seu peso ideal'
elif imc >= 25 and imc < 30:
    status = 'acima de seu peso ideal'
elif imc >= 30 and imc < 40:
    status = 'com no estado de obesidade'
else:
    status = 'com no estado de obesidade morbida'

print(f'O seu imc é de{imc:.1f}, portanto você está {status}. ')
