class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRow(row):
            nums = [x for x in board[row] if x != '.']
            return len(nums) == len(set(nums))
        def isValidCol(column):
            nums = []   
            for i in range(9):
                if board[i][column] != '.':
                    nums.append(board[i][column])
            return len(nums) == len(set(nums))      
        def isValidSquare(row, col):
            nums=[]
            for i in range(3):
                for j in range(3):
                    if board[row+i][col+j] != '.':
                        nums.append(board[row+i][col+j])
            return len(nums) == len(set(nums))
        for i in range(9):
            if not isValidRow(i) or not isValidCol(i):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not isValidSquare(i, j):
                    return False
        return True

               

