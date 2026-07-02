# 119. Pascal's Triangle II - Easy
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [None] * (rowIndex+1)
        row[0] , row[-1]= 1, 1
        for i in range(1, rowIndex):
            row[i] = row[i-1] * (rowIndex - i + 1) // i 
        return row 