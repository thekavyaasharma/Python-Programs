# revrse number to check if its palindrom 
# 121 = 121 palindrome

num = int(input("ENTER A NUMBER: "))
temp = num
rev = 0

while temp != 0:
    digit = temp % 10       # takes last digit out 
    rev = rev * 10 + digit  # ads digit to rev 
    temp //= 10             # removes the last digit 

if rev == num:
    print(f"The reverse of {num} is {rev} and is palindrom")
else:
    print(f"The reverse of {num} is {rev} and  is not a plaindrom number")


# use slicing to reverse 
print("Using slicing to reverse the number")

n = str(num)
n = n[::-1]
print(f"The reverse number is {n}")

# reverse number upto 32 bits else return 0 : leetcode

s = str(abs(x))
rev = int(s[::-1])

res = rev if x > 0 else -rev

if res < -2**31 or res > 2**31 -1:
    print(0)
else:
    print(res)

