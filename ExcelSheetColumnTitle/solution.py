class Solution(object):
    def convertToTitle(self, columnNumber):
        s = ""
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            s = chr(offset + ord('A')) + s
            columnNumber = (columnNumber - 1) // 26
        return s
    
solution = Solution()

print(solution.convertToTitle(701)) # prints ZY