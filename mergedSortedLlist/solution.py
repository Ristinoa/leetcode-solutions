# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Problem: can't figure out how to return the head of the merged list
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
        
            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next


input1 = ListNode(1)
input1.next = ListNode(2)
input1.next.next = ListNode(4)

input2 = ListNode(1)
input2.next = ListNode(3)
input2.next.next = ListNode(4)

solution = Solution()
print(solution.mergeTwoLists(input1,input2))
# Prints the address of the head of the merged list