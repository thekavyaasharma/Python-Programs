# array = [11,12,13] -> [1,1,1,2,1,3]

def separate_digits(nums):
    n = len(nums)
    res = []

    for i in nums:
        for ch in str(i):
            res.append(int(ch))

    return res

nums = [1,22,98,1867]

print(f'original array: \n{nums}')
print('Separated digits in array: ')
print(separate_digits(nums))

def sep2(num):
    n = len(num)
    result = []

    for i in range(n-1,-1,-1):
        x = num[i]
        while x!=0:
            result.append(x%10)
            x //=10

    return result[::-1]
                
    
    
nums = [1,22,98,1867]

y = sep2(nums)

print(y)