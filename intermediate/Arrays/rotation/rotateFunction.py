# array = [4,3,2,6]  aaray len = 4 f(0-3)
# f(0) : 0 * 4 + 1*3 + 2*2 +3*6 = sum1
# f(1) = 0*6 + 1*4 +2*3 +3*2 = sum2
# f(2) last element first = sum3
# f(3) last element first = sum 4

arr = [4,3,2,6]

n = len(arr)
total = sum(arr)
fn = sum(index*value for index, value in enumerate(arr))
max_val = fn

for i in range(1,n):
    fn = fn + total - n * arr[n-i]
    max_val = max(max_val,fn)

print(max_val)