from typing import List


class Solution:
    @staticmethod
    def satisfiesConditions(grid: List[List[int]]) -> bool:
        for i in range(len(grid[0])):
            for j in range(len(grid)-1):
                if grid[j][i]!=grid[j+1][i]:
                    return False                
        
        for i in range(len(grid)):
            k=0
            for j in range(len(grid[0])):
                if k+1<len(grid[0]) and grid[i][k] == grid[i][k+1]:
                    return False
                k+=1
        
        return True
            

# grid = [[1,0,2],[1,0,2]]
# grid = [[1],[2],[3]]
# grid = [[0]]
grid = [[2,4,5,9,0,0,7,3,9,9]]
print(Solution.satisfiesConditions(grid))