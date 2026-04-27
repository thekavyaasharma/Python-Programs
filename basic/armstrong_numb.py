# armstrong number/ narcissist : 153 : 1cube + 5 cube + 3 cube = 153
# 1634 -> 1**4 + 6**4 + 3**4+ 4**$
user_input = (input("ENTER A NUMBER TO CHECK IF ITS ARMSTRONG: "))
power = len(user_input)
user_input = int(user_input)
temp = user_input 

sum = 0

while temp != 0:
    sum += (temp % 10 )**power # extracting last digit and multipying it with power
    temp = temp//10 # removing last digit

if user_input == sum :
    print(f'{user_input} is an Armstrong number')
else:
    print(f'{user_input} is not an Armstrong number')