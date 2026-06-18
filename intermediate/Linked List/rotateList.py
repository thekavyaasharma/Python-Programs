# 61 - ROTATE LIST - MEDIUM 

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head 

        n = 1
        tail = head
        while tail.next:
            tail = tail.next 
            n +=1
        
        k = k % n 
        if k == 0:
            return head 
    
        tail.next = head

        steps = n - k 
        new_tail = head

        for _ in range(1,steps):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head 
