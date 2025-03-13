class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRows = {}
        seenCols = {}
        seenSquares = {}

        for i in range(9):
            seenRows[i] = set()
            seenCols[i] = set()
            seenSquares[i] = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                
                num = board[i][j]
                    
                if num in seenRows[i] or num in seenCols[j] or num in seenSquares[(i//3)*3 + (j//3)]:
                    return False

                seenRows[i].add(num)
                seenCols[j].add(num)
                seenSquares[(i//3)*3 + j//3].add(num)
        
        return True
