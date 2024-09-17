# Definition for singly-linked list.
# Iterative solution, very inefficient

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        seen = []

        dummyHead = head

        while dummyHead is not None:
            if dummyHead not in seen:
                seen.append(dummyHead)
                dummyHead = dummyHead.next
            else:
                return True
        
        return False
            
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

solution = Solution()

print(solution.hasCycle(head)) # returns True