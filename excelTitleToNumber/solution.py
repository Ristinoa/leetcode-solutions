class Solution(object):

    def titleToNumber(self, columnTitle):
        c = 0
        for ch in columnTitle:
            current = ord(ch) - ord('A') + 1
            c = c * 26 + current
        
        return c
    
solution = Solution()

print(solution.titleToNumber("A")) # Prints 1
print(solution.titleToNumber("BC")) # Prints 55
print(solution.titleToNumber("ZY")) # Prints 701