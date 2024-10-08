# validPalindrome solution

class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        
        return True

solution = Solution()

s = "A man, a plan, a canal: Panama"
s2 = "race a car"

print(solution.isPalindrome(s)) # Prints True
print(solution.isPalindrome(s2)) # Prints False
