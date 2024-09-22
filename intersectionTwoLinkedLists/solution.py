# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB

        while (a != b):
            if not a:
                a = headB
            else:
                a = a.next
            if not b:
                b = headA
            else:
                b = b.next
        
        return a
    
a1 = ListNode(4)
a2 = ListNode(1)

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(1)

c1 = ListNode(8)
c2 = ListNode(4)
c3 = ListNode(5)

# A

headA = a1
headA.next = a2
headA.next.next = c1
headA.next.next.next = c2
headA.next.next.next.next = c3

# B

headB = b1
headB.next = b2
headB.next.next = b3
headB.next.next.next = c1
headB.next.next.next.next = c2
headB.next.next.next.next.next = c3

solution = Solution()

print(solution.getIntersectionNode(headA, headB)) # Prints ID of c1 
print(c1) # For verification

