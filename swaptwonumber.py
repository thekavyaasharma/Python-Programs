# swap two numbers : 3 ways

def tempvar(a,b):
    """ using temproray variable to swap two numbers"""
    temp = a
    a = b
    b = temp

    print(f'a is {a} b is {b}')

def addsub(a,b):
    """ using addition and subtraction to swap two numbers"""
    a = a+b
    b = a-b
    a = a-b

    print(f'a is {a} b is {b}')

def bitwiseops(a,b):
    """ using XOR to swap two vars  """
    a = a^b
    b = b^a
    a = a^b

    print(f'a is {a} b is {b}')

a,b = int(input(' a : ')), int(input(' b : '))

tempvar(a,b)
print(tempvar.__doc__)

addsub(a,b)
print(addsub.__doc__)

bitwiseops(a,b)
print(bitwiseops.__doc__)
