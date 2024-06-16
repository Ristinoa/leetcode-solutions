class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        numerals = {"I":1, "V": 5, "X":10, "L":50 ,"C": 100, "D":500, "M":1000}
        output = 0
        i = 0

        while i < len(s):
            if i == len(s) - 1:
                output += numerals[s[i]]
                i += 1
            elif numerals[s[i]] < numerals[s[i + 1]]:
                twoPart = numerals[s[i + 1]] - numerals[s[i]]
                output += twoPart
                i += 2
            else:
                output += numerals[s[i]]
                i += 1
        
        return output
    
solution = Solution()

input1 = "III"
print(solution.romanToInt(input1))

input2 = "LVIII"
print(solution.romanToInt(input2))

input3 = "MCMXCIV"
print(solution.romanToInt(input3))