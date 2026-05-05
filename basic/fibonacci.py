# finonacci : 0,1,1,2,3,5,8,13,21,34

n = int(input("Enter a number: "))

a = 0
b = 1
print(a,b,end=" ")

for _ in range(n-1):
    c = a+b
    a,b = b,c
    print(c, end=" ")
    
print()

'''
           fib(4)
          /      \
      fib(3)  +  fib(2)
      /    \      /    \
  fib(2) + fib(1)fib(1) + fib(0)
  /    \
fib(1)+fib(0)

'''

# function 
def fibonacci(n):
    if n <=1:
        return n
    a = 0
    b = 1
    for _ in range(n):
        a,b = b, a+b

    return a

res = fibonacci(n)
print("Using simple function to print fibonacci series: ", res )








# recursion
def fib_rec(n):
    if n <=1:
        return n
    
    return fib_rec(n-1) + fib_rec(n-2)

res = fib_rec(n)
print("Using rescursion: ", res)






