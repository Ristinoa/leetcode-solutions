# Current solution is O(n^2) this can be done faster

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i == j):
                    continue
                else:
                    if (nums[i] + nums[j] == target):
                        output.append(i)
                        output.append(j)
                        return output
                    else:
                        continue
                j += 1
            i += 1

# test cases:
solution = Solution()

nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums, target)) # prints out [0, 1]
print("\n")

nums = [3,2,4]
target = 6
print(solution.twoSum(nums, target)) # prints out [1, 2]
print("\n")

nums = [3,3]
target = 6
print(solution.twoSum(nums, target)) # prints out [0, 1]
print("\n")

