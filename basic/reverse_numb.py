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

# using recursion 