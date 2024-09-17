# Two-pointer approach, runs much faster than the looping version

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

solution = Solution()

print(solution.hasCycle(head)) # returns True