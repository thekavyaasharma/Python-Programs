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