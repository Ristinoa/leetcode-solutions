# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preorder traversal:
        
class Solution(object):
    def preorderTraversal(self, root):
        result = []

        def preorder(node):

            if not node:
                return

            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)

        return result
    
solution = Solution()

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)

root.right = node1
node1.left = node2

print(solution.preorderTraversal(root)) # returns [1,2,3]


