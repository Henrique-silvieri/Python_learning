def currency(num):
    return f'R${num:.2f}'


def increase(num, percentage, show=False):
    p = percentage / 100
    total = num + (num * p)
    if show:
        return f'R${total:.2f}'
    else:
        return total
    
    
def decrease(num, percentage, show=False):
    p = percentage / 100
    total = num - (num * p)
    if show:
        return f'R${total:.2f}'
    else:
        return total
    

def double(num, show=False):
    d = float(num * 2)
    if show:
        return f'R${d:.2f}'
    else:
        return d
    

def half(num, show=False):
    h = float(num / 2)
    if show:
        return f'R${h:.2f}'
    else:
        return h

def summary(num, inc, dec):
    print('=' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('=' * 30)
    
    print(f'{"Preço analisado:":<20}{"R$":>4}{num}')
    print(f'{"Dobro do preço:":<20}{"R$":>4}{num*2}')
    print(f'{"Metade do preço:":<20}{"R$":>4}{num/2}')
    
    p1 = inc / 100
    p2 = dec / 100
    total1 = num + (num * p1)
    total2 = num - (num * p2)
    print(f'{inc}%{" de aumento":<17}{"R$":>4}{total1}')
    print(f'{dec}%{" de aumento":<17}{"R$":>4}{total2}')
    print('=' * 30)
