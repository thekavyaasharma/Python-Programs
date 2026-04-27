# using temp var 
a,b = int(input("ENTER A: ")), int(input("ENTER B: "))
temp = a
a=b
b=temp 
print(f"using temp variable.\n A: {a}, B:{b}")

# using add and subtrat 
print("\n using addition and subtraction method")
a,b = int(input("ENTER A: ")), int(input("ENTER B: "))

a = a-b  # 10 - 200 -> -190
b = b+a # 200- 190 = 10
a = b-a # 10 - (-190) = 200

print(f'A : {a}, B : {b}')

# using bitwise manipultion : XOR
print("\n using bitwise manipulation method")
a,b = int(input("ENTER A: ")), int(input("ENTER B: "))


# returns 1 if bits are different
# a= 5, b = 2: 101^10 = 111(7)


a = a^b  
b = a^b  # 111^10= 101(5)
a = a^b  # 111^101 = 010(2)

print(f'A : {a}, B : {b}')
