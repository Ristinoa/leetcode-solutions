# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):

        def inOrder(root, arr):
            if not root:
                return
            else:
                inOrder(root.left, arr)
                arr.append(root.val)
                inOrder(root.right, arr)
            
            return arr
        
        return inOrder(root, [])


left2 = TreeNode(3)
left1 = TreeNode(2, left2)
root = TreeNode(1, left1)

solution = Solution()
print(solution.inorderTraversal(root)) # prints [3, 2, 1]