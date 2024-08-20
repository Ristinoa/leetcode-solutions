# CREDIT: Timothy H Chang
# ? Link: https://www.youtube.com/watch?v=xdFzPCa9g4A

class Solution(object):

    # Strategy: traverse from princess to knight
    # ! Need to deal with [[0,0]] issue <-- current solution has out of bounds error

    def calculateMinimumHP(self, dungeon):
        height, width = len(dungeon), len(dungeon[0])
        m, n = height - 1, width - 1

        # princess dungeon
        pd = dungeon

        # princess room 
        pd[m][n] = max(1, 1 - dungeon[m][n])

        # Populate straight right
        for r in range (m - 1, -1, -1):
            pd[r][n] = max(1, pd[r + 1][n] - pd[r][n])
        
        # Populate straight down
        for c in range(n - 1, -1, -1):
            pd[m][c] = max(1, pd[c + 1][n] - pd[m][c])
        
        # Rest of princess dungeon (legal moves)
        for r in range(m - 1, -1, -1):
            for c in range(n -1, -1, -1):
                # crucial step: determine HP using legal acess points
                pd[r][c] = max(1, min(pd[r + 1][c], pd[r][c+1]) - pd[r][c])
        
        return pd[0][0]

solution = Solution()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]

print(solution.calculateMinimumHP(dungeon)) # Prints out 7


