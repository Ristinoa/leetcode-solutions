from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        m = defaultdict(int)

        for num in nums:
            m[num] += 1
        
        n = n // 2
        for key, value in m.items():
            if value > n:
                return key
        
        return 0
    
input = [1,1,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,1,2,2]
solution = Solution()

print(solution.majorityElement(input)) # prints 1