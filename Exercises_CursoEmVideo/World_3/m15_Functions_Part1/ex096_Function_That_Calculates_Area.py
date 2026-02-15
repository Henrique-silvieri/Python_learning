# Create a program that has a function called area(), which receives the dimentions of a rectangular plot of land (length and weight) 
# and display the area of the land.

def area(width, lenght):
    area = width * lenght
    print(f'A área do terreno é de {width:.2f}m X {lenght:.2f}m = {area:.2f}m²')


w = float(input('Qual é a largura do terreno em metros? '))
l = float(input('Qual é o comprimento do terreno em metros? '))
area(w, l)