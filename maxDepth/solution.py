# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return 1 + max(leftDepth, rightDepth)

solution = Solution()

right2 = TreeNode(5)
left2 = TreeNode(4)

right1 = TreeNode(3,None, right2)
left1 = TreeNode(2,None, left2)

root = TreeNode(1,left1, right1)

print(solution.maxDepth(root))