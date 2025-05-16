# Create a program that reads the weight of five people. In the end, show which was the highest and lowest weight read.

heavier =  0
lighter = 0
for i in range(5):
    weight = float(input(f'Digite o peso da pessoa n°{i+1}: '))
    if weight == 1:
        heavier = weight
        lighter = weight
    else:
        if weight > heavier:
            heavier = weight
        if weight < lighter:
            lighter = weight

print(f'O maior peso da lista é {heavier} e menor peso da lista é {lighter}')
