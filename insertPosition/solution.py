class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
            if nums[i] > target:
                return i
        
        return (len(nums))

solution = Solution()
nums = [1,3,5,6]
target = 5

print(solution.searchInsert(nums, target))