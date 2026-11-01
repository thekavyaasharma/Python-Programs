# 1855. Maximum Distance Between a Pair of Values - Medium
class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        i =j = 0
        while i < len(nums1) and j< len(nums2):
            i+= nums1[i] > nums2[j]
            j+=1
        return max(0,j-i-1)
        