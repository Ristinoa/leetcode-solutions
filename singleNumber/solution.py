# Iterative solution, very slow (can be done faster)

class Solution(object):
    def singleNumber(self, nums):
        seen = []
        for num in nums:
            if num not in seen:
                seen.append(num)
            else:
                seen.remove(num)
        
        return seen[0]
    
solution = Solution()
input1 = [2,2,1]
input2 = [4,1,2,1,2]
input3 = [1]

print(solution.singleNumber(input1)) # prints 1
print(solution.singleNumber(input2)) # prints 4
print(solution.singleNumber(input3)) # prints 1