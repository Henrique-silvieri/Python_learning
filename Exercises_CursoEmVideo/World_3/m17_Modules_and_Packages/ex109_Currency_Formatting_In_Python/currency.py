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
