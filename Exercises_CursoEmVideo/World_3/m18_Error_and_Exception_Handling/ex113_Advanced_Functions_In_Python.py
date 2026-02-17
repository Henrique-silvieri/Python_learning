# Rewrite the readInt() function that we did in challenge 104, now including the possibility of entering an invalid number type. 
# Also, create a function called readFloat() with the same functionality.

def readInt(intNum):
    while True:
        try:
            value = int(input(intNum))
        except (ValueError, TypeError):
            print('\033[0;31mERRO, digite um numero inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mA entrada de dados foi interrompida.\033[m')
            return 'Nenhum'
        else:
            return value

def readFloat(floatNum):
    while True:
        try:
            value = float(input(floatNum))
        except (ValueError, TypeError):
            print('\033[0;31mERRO, digite um numero inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mA entrada de dados foi interrompida.\033[m')
            return 'Nenhum'
        else:
            return value


n1 = readInt('Digite um número inteiro: ')
n2 = readFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o número real digitado foi ')











































# def readInt(intValue=0):
#     value = 0
#     while True:
#         number = str(input(intValue))
#         if not number.isalpha():
#             value = int(number)
#             break
#         else:
#             
#     return value

# def readFloat(floatValue=0):
#     value = 0
#     while True:
#         number = str(input(floatValue))
#         if not number.isalpha():
#             value = float(number)
#             break
#         else:
#             print('\033[0;31mERRO, digite um numero real válido.\033[m')
#     return value


# try:
#     intNumber = readInt('Digite um número inteiro: ')
# except ValueError:
#     while True:
#         print('\033[0;31mERRO, digite um numero inteiro válido.\033[m')
#         intNumber = readInt('Digite um número inteiro: ')

# try:
#     floatNumber = readFloat('Digite um número real: ')
# except ValueError:
#     while True:
#         print('\033[0;31mERRO, digite um numero real válido.\033[m')
#         floatNumber = readFloat('Digite um número real: ')

# finally:
#     print(f'O número inteiro é {intNumber}, e o número real é {floatNumber}')
