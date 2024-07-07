# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop(0)

            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            
            if node.right:
                queue.append((node.right, depth +1))
        
        return 0

root = TreeNode(3)
root.right = TreeNode(20)
root.left = TreeNode(9)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)

sol = Solution()
print(sol.minDepth(root)) # returns 2