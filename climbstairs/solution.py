# This is another cool solution, uses memoization to store previously computed calculations

class Solution(object):
    def climbStairs(self, n):
        # store computations in cache to be used in recursive loop
        # avoids redundant calculations, saves on runtime
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        # base cases, to get to the zeroth or 1st step, there's only one way
        if n == 0 or n == 1:
            return 1
        # apply memoization here
        if n not in memo:
            # use two different recursive loops to track 1 or 2 steps
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]

solution = Solution()
print(solution.climbStairs(45))
print(solution.climbStairs(13))
print(solution.climbStairs(2))
