# Create a program that has a function called vote() which will receive a person's birth year as a parameter, 
# returning a literal value indicating if that person's vote is DENIED, OPTIONAL, or MANDATORY in the elections.

def vote(year):
    from datetime import datetime    
    age = datetime.now().year - year
    if 65 > age >= 18:
        return f'Com {age} anos, o voto é: OBRIGATÓRIO'
    elif age >= 65 or 18 > age >= 16:
        return f'Com {age} anos, o voto é: OPCIONAL'
    else:
        return f'Com {age} anos, o voto é: NEGADO'
    
birthYear = int(input('Digite seu ano de nascimento: '))
print(vote(birthYear))