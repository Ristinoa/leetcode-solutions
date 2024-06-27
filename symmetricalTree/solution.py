# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isMirrored(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirrored(left.left,right.right) and self.isMirrored(left.right, right.left)

    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirrored(root.left, root.right)

l2 = TreeNode(3)
r2 = TreeNode(3)
r1 = TreeNode(2, l2, None)
l1 = TreeNode(2, None, r2)
root = TreeNode(1, r1, l1)
solution = Solution()
print(solution.isSymmetric(root))