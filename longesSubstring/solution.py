class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        charSet = set()
        l = 0
        output = 0
        
        for r in range (len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            output = max(output, r - l + 1)
        
        return output

solution = Solution()

case1 = "abcabcbb"
print(solution.lengthOfLongestSubstring(case1))

case2 = "bbbbb"
print(solution.lengthOfLongestSubstring(case2))

case3 = "pwwkew"
print(solution.lengthOfLongestSubstring(case3))