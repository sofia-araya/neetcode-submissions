class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = [set() for _ in range(9)]
        cols_seen = [set() for _ in range(9)]
        boxes_seen = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                current = board[i][j]
                box_idx = (i//3) * 3 + (j//3)
                if current == ".":
                    continue

                if current in rows_seen[i] or current in cols_seen[j] or current in boxes_seen[box_idx]:
                    return False

                rows_seen[i].add(current)
                cols_seen[j].add(current)
                boxes_seen[box_idx].add(current)
            
        return True

                

        