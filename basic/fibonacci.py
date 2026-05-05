# finonacci : 0,1,1,2,3,5,8,13,21,34

n = int(input("Enter a number: "))

a = 0
b = 1
print(a,b,end=" ")
i = 0
while i < n:
    c = a+b
    a,b = b,c
    print(c, end=" ")
    i+=1



