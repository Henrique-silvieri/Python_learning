def increase(num, percentage):
    p = percentage / 100
    total = num + (num * p)
    return total
    
    
def decrease(num, percentage):
    p = percentage / 100
    total = num - (num * p)
    return total
    

def double(num):
    d = float(num * 2)
    return d
    

def half(num):
    h = float(num / 2)
    return h
