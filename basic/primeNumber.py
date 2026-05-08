# prime numer : 2,3,5,7,11,13,17 others are composite 
# 1 is neither prime nor composite.
# A natural number n > 1 : is prime if its only divisors are 1 and n.
# 2 is the smallest prime number and the only even prime number.

number = int(input("Enter a number to check if it is prime or composite: "))

i = 2

while i <= number//2:

    if number % i == 0:
        print(f"{number} is a composite number.")
        break
    
    i+=1

else:
    print(f"{number} is a Prime number.")

    