# Write a program that reads a temperature in °C and converts it to °F.

celcius = float(input('Digite a temperatura em °C: '))
fahrenheit = (celcius * 9/5) + 32

print(f'A temperatura {celcius}°C, convertida para fahrenheit é de {fahrenheit}°F.')
