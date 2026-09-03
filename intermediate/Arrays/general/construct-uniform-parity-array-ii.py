# 3876. Construct Uniform Parity Array II - Medium
class Solution(object):
    def uniformArray(self, nums1):
        smallestOdd = float('inf')

        for i in nums1:
            if i % 2 == 1:
                smallestOdd = min(smallestOdd, i)
        
        if smallestOdd == float('inf'):
            return True
        else:
            for i in nums1:
                if i < smallestOdd :
                    return False
            return True
        