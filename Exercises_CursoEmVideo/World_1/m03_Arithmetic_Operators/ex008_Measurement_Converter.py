# Write a program that reads a value in meters and displays it converted into centimeters and millimeter.

value = float(input('Digite um valor em metros: '))
centimeter = value * 100
millimeter = value * 1000
print(f'O valor {value}m, vale {centimeter}cm e {millimeter}mm')
