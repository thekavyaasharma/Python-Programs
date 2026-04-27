# using temp var 
a,b = int(input("ENTER A: ")), int(input("ENTER B: "))
temp = a
a=b
b=temp 
print(f"using temp variable.\n A: {a}, B:{b}")

