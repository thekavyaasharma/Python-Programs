n = int(input("Enter number of rows: "))
cnt = 0
for i in range(n):
    x = n-1-i
    print(" " * x, end ="")
    print("*", end="")
    if 0 <i<n-1:
        sp = cnt + i
        print(" " * sp, end="")
        print("*")
        cnt+=1
    elif i == n - 1:
        print("*"* (i*2) )
    else:
        print()