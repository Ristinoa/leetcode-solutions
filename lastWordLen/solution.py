class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not ' ' in s:
            return(len(s))
            
        sList = list(filter(None, s.split()))

        if len(sList) == 1:
            return(len(sList[0]))
        else:
            return(len(sList[-1]))

solution = Solution()
input1 = "    day"
input2 = "Hello World"
input3 = "   Suh dude   "

print(solution.lengthOfLastWord(input1))
print(solution.lengthOfLastWord(input2))
print(solution.lengthOfLastWord(input3))
