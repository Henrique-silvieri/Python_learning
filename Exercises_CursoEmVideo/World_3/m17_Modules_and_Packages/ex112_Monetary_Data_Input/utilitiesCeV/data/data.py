def readMoney(prompt):
    isValid = False
    while not isValid:
        inpt = str(input(prompt)).replace(',', '.').strip()
        if inpt.isalpha() or inpt == '':
            print(f'\033[0;31mERRO, digite um preço valido.\033[m')
        else:        
            isValid = True
            return float(inpt)