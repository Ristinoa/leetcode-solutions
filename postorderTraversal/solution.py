# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []

        def postorder(node):
            if not node:
                return
            
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
        
        postorder(root)
        
        return result

solution = Solution()

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)

root.right = node1
node1.left = node2

print(solution.postorderTraversal(root)) # returns [3,2,1]
    
