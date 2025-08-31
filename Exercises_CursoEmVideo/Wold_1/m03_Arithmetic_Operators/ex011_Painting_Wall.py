# Create a program that reads the height and width of a wall (in meters), calculates its area, and shows how much paint will be needed to paint it, considering that each liter of paint covers 2m².

height = float(input('Qual a altura da parede em metros? '))
width = float(input('Qual a largura da parede em metros? '))
area = height * width
paint_needed = area / 2
print(f'A área da parede é de {area} m², portanto a quantidade de tinta necessária de {paint_needed} L')
