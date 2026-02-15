# Create a program that has a function called factorial() that receives two parameters: the first to indicate the number to calculate, 
# and the other called show, which will be a logical (boolean) value (optional) indicating whether or not the factorial calculation process 
# will be displayed on the screen.

def factorial(n, show=False):
    """"
    factorial (n, show)
    :param n: The number to be calculated.
    :param show: (Optional) Display or not the math problem.
    :return: The factorial value of a n number.
    """
    
    f = 1
    if show == False:
        for c in range(n, 0, -1):
            f *= c
        return f
    else:
        for c in range(n, 1, -1):
            f *= c
            print(f'{c} X ', end='')
        return f'1 = {f}'
    
    
    
print(factorial(2))
help(factorial)