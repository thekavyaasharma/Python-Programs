# 463 EASY
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        islandCount = 0
        neighbours = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    islandCount +=1
                    if i < row -1 and grid[i+1][j] == 1:
                        neighbours +=  1
                    if j < col -1 and grid[i][j+1] == 1:
                        neighbours += 1
        return islandCount * 4 - neighbours *2  



class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        perimeter = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] ==1:
                    # up 
                    if i == 0 or grid[i-1][j] == 0:
                        perimeter +=1
                    # left
                    if j == 0 or grid[i][j-1] == 0:
                        perimeter +=1
                    # down 
                    if i == row - 1 or grid[i+1][j] == 0:
                        perimeter +=1
                    # right 
                    if j == col -1 or grid[i][j+1] == 0:
                        perimeter +=1
        return perimeter 