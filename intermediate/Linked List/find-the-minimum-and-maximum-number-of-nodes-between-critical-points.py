# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points - Medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        while head :
            nums.append(head.val)
            head = head.next

        n = len(nums)
        ind = []
        for i in range(1,n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                ind.append(i)
            elif nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                ind.append(i)

        m = len(ind)
        if m < 2:
            return [-1,-1]
        min_dist = inf
        max_dist = ind[-1] - ind[0]

        for i in range(1,m):
            min_dist = min(min_dist, ind[i] - ind[i-1])
        
        return [min_dist, max_dist]

        