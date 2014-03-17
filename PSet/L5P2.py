def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 1:
        return base
    return base * recurPower(base, exp - 1)

base = float(raw_input('Enter base: '))
exp = int(raw_input('Enter exp: '))
print recurPower(base, exp)