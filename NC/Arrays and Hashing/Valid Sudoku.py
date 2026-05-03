from collections import Counter, defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=set()
        cols=set()
        boxes=defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val!='.' and val in rows:
                    return False
                rows.add(val)

                val = board[j][i]
                if val!='.' and val in cols:
                    return False
                cols.add(val)

                box_id = (i//3,j//3)
                val = board[i][j]
                if val!='.' and val in boxes[box_id]:
                    return False
                boxes[box_id].add(val)
            rows=set()
            cols=set()
        return True
    
# R1
# Recommended TS Complexity
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen=defaultdict(set)
        col_seen=defaultdict(set)
        box_seen=defaultdict(set)
        for i in range(9):
            for j in range(9):

                val=board[i][j]
                box_key=(i//3,j//3)

                if val!='.':
                    if val in row_seen[i] or val in col_seen[j] or val in box_seen[box_key]:
                        return False
                
                    row_seen[i].add(val)
                    col_seen[j].add(val)
                    box_seen[box_key].add(val)

        return True
