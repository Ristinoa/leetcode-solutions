class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = len(digits) - 1

        while(digits[i] == 9 and i >= 0):
            if (i == 0):
                output = [0] * (len(digits) + 1)
                output[0] = 1
                return(output)
            
            digits[i] = 0
            i -= 1
        
        digits[i] += 1
        return digits

solution = Solution()
input1 = [1,2,3]
input2 = [9,9,9,9]
print(solution.plusOne(input1))
print(solution.plusOne(input2))