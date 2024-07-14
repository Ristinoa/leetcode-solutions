# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):

        if not root: # case for if tree is empty
            return False

        if not root.right and not root.left:
            return root.val == targetSum
        
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)
    
        return left_sum or right_sum
    
solution = Solution()

# [5,4,8,11,null,13,4,7,2,null,null,null,1]

root = TreeNode(5)
root.right = TreeNode(8)
root.right.right = TreeNode(4)
root.right.left = TreeNode(13)
root.right.right.right = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

print(solution.hasPathSum(root, 22))