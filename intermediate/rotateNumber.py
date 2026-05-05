# numbers : 0 , 1 , 8 , 2 , 5, 6, 9 are valid : when roated to 180d they become a number
# numbers : 2, 4, 6, 9 are form different numbers when rotated unlike 0, 1, 8
# print total numbers from 0 - n which follow these two rules 


def rotate_num(number):
    counter = 0 
    if number == 0:
        return 0

    for i in range(number+1):
        temp = i
        is_valid = True
        has_changed = False

        while temp > 0:
            digit = temp % 10

            if digit==3 or digit == 4 or digit==7:
                is_valid = False
                break

            elif digit==2 or digit ==5 or digit ==6 or digit ==9:
                has_changed = True
            
            temp //= 10
        
        if is_valid == True and has_changed ==True:
            counter +=1
    
    return counter 

num = int(input("Enter a number: ")) # teset cases : 0, 5 , 10 , 20 , 100

res = rotate_num(num)
print(res)


