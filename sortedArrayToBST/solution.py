# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        # Note: Median value tends to be the root
        terms = len(nums)
        if not terms:
            return None

        middle_val = terms // 2
        return TreeNode(
            nums[middle_val], self.sortedArrayToBST(nums[:middle_val]),  self.sortedArrayToBST(nums[middle_val + 1:])
        )
    
input = [-12, -11, -10, -3, 0, 1, 2, 7, 9]
solution = Solution()
print(solution.sortedArrayToBST(input)) # prints address of head node