# Write a program that reads the name of a city and says whether or not it starts with "SANTO"

city = input('Digite o nome da sua cidade: ').strip()
print(city[:5].upper() == 'SANTO')
