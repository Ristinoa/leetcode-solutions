# Better solution for singleNumber problem
# Uses bitwise xOR

class Solution:
    def singleNumber(self, nums):
        answer = 0
        for num in nums:
            answer ^= num
        return answer

solution = Solution()
input1 = [2,2,1]
input2 = [4,1,2,1,2]
input3 = [1]

print(solution.singleNumber(input1)) # prints 1
print(solution.singleNumber(input2)) # prints 4
print(solution.singleNumber(input3)) # prints 1
