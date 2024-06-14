class Solution(object):

    def minIncrementForUnique(self, nums):
        nums.sort()
        output = 0

        for i in range(1, len(nums)):           
            if nums[i] <= nums[i - 1]:
                    increment = nums[i - 1] - nums[i] + 1
                    nums[i] += increment
                    output += increment

        return output

solution = Solution()

input1 = [1,2,2]
print(solution.minIncrementForUnique(input1))

input2 = [3,2,1,2,1,7]
print(solution.minIncrementForUnique(input2))

# works with massive inputs as well
