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