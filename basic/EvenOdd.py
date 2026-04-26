# take input from user
a = int(input("Enter a number: "))

# using % operator 
print("Checking even odd using modulo operator")
if a % 2 == 0 :
    print(a, " is an even number.")
else:
    print(a, " is an odd numebr.")

#  using ternary condition 
print("Using ternary operations")
print("EVEN" if a % 2 == 0 else "ODD")

# using bitwise operations 
print("Using bitwise manipulation")
if a & 1:
    print(a, "is odd")
else:
    print(a, " is even")

