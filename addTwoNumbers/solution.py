class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        outputList = ListNode()
        currentNode = outputList
        carry = 0

        while l1 or l2 or carry:
            sumTotal = carry

            if l1:
                sumTotal += l1.val
                l1 = l1.next
            if l2:
                sumTotal += l2.val
                l2 = l2.next
            
            carry = sumTotal // 10
            sumTotal %= 10

            currentNode.next = ListNode(sumTotal)
            currentNode = currentNode.next
        
        return outputList.next

solution = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = solution.addTwoNumbers(l1, l2) # Prints 7 0 8

while result:
    print(result.val, end=" ")
    result = result.next