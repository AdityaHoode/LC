class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        for row in matrix:
            if target>=row[0] and target<=row[-1]:
                l,r=0,len(row)-1
                while l<=r:
                    m=(l+r)//2
                    if target>row[m]:
                        l=m+1
                    elif target<row[m]:
                        r=m-1
                    else:
                        return True
        return False

# Recommended TS Complexity
class Solution:
    def binarySearchMatrix(self, matrix: List[List[int]], target: int) -> int:
        l,r=0,len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if target>matrix[m][-1]:
                l=m+1
            elif target<matrix[m][0]:
                r=m-1
            else:
                return m
        return -1

    def binarySearchRow(self, row: List[int], target: int) -> bool:
        l,r=0,len(row)-1
        while l<=r:
            m=(l+r)//2
            if target>row[m]:
                l=m+1
            elif target<row[m]:
                r=m-1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index=self.binarySearchMatrix(matrix, target)
        if index!=-1:
            return self.binarySearchRow(matrix[index], target)
        else: 
            return False
        
# Interview ready
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        l,r=0,(rows*cols)-1
        while l<=r:
            m=(l+r)//2
            row=m//cols
            col=m%cols
            if target>matrix[row][col]:
                l=m+1
            elif target<matrix[row][col]:
                r=m-1
            else:
                return True
        return False