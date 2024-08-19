# ! This solution is VERY slow and can be optimized to O(rowIndex) running time

class Solution(object):
    def getRow(self, rowIndex):
        # set up output row
        output = [0] * (rowIndex + 1)
        output[0] = 1

        # iteratively populate the row with values from previous rows
        for row in range(1, rowIndex + 1):
            output[row] = 1
        
            # use iteration to correctly add values at each level
            for index in range(row - 1, 0, -1):
                output[index] += output[index - 1]

        return output

solution = Solution()
print(solution.getRow(4))