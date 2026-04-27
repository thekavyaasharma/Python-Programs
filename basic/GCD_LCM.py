#GCD: greatest common divisor : use math.gcd() and math.lcm()

# lcm(a,b) = a*b / gcd(a,b)
def gcd(a,b):
    while b !=0 :
        a,b = b, a%b # if a <B -> a%b = a
    return a

# LCM : least common multiple 
def lcm(a,b):
    if a ==0  or b ==0:
        return 0 
    return abs(a*b)//gcd(a,b)

a,b = int(input("ENTER A NUMBER: ")), int(input("ENTER ANOTHER NUMBER: "))
l = lcm(a,b)
print(f'The LCM of {a} and {b} is {l}') 