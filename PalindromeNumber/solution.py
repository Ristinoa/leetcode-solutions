class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        rev = strx[::-1]

        i = 0

        while i < len(strx):
            if strx[i] != rev[i]:
                return False
            else:
                i += 1
        
        return True

solution = Solution()
x = 121
print(solution.isPalindrome(x))

x1 = -121
print(solution.isPalindrome(x1))

x2 = 10
print(solution.isPalindrome(x2))