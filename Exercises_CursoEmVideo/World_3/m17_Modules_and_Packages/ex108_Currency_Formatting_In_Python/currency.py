def currency(num):
    return f'R${num:.2f}'


def increase(num, percentage):
    p = percentage / 100
    total = num + (num * p)
    return f'R${total:.2f}'
    
    
def decrease(num, percentage):
    p = percentage / 100
    total = num - (num * p)
    return f'R${total:.2f}'
    

def double(num):
    d = float(num * 2)
    return f'R${d:.2f}'
    

def half(num):
    h = float(num / 2)
    return f'R${h:.2f}'
