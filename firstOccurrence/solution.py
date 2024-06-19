class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        matching = True
        k = 0

        if len(haystack) < len(needle):
            return -1
        
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
    

haystack = "sadbutsad"
needle = "sad"
solution = Solution()

print(solution.strStr(haystack, needle))