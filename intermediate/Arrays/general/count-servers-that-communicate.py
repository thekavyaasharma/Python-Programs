# 1267. Count Servers that Communicate - Medium
class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and rows[i]+cols[j]>2:
                    ans+=1
        return ans

        