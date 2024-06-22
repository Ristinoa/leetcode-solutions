class Solution(object):
    # This solution is interesting, as it uses a binary search implementation to determine a square root (rounded)
    def mySqrt(self, x):
        left = 0
        right = x 
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        
        return right

solution = Solution()

print(solution.mySqrt(4))
print(solution.mySqrt(5))
print(solution.mySqrt(144))