# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        # Solution is recursive DFS
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False
    
input1 = TreeNode(3)
input2 = TreeNode(2)
input = TreeNode(1,input2, input1)
inputTree2 = input
inputTree3 = TreeNode(1, input1, input2)
solution = Solution()

print(solution.isSameTree(input, inputTree2)) # Returns True
print(solution.isSameTree(input, inputTree3)) # Returns False


