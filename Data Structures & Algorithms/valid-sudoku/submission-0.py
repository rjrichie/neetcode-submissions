class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ret = True
        for row in board:
            ret = ret and self.checkValidRow(row)
        ret = ret and self.checkColumns(board)
        ret = ret and self.checkBox(board)

        return ret


    def checkValidRow(self, row: List[str]):
        hm = defaultdict(list)
        for r in row:
            if r == ".":
                continue
            hm[r] = 1 + hm.get(r, 0)
        for val in hm.values():
            if val > 1:
                return False
        return True
    
    def checkColumns(self, board: List[List[str]]):
        for i in range(9):
            hm = defaultdict(list)
            for j in range(9):
                if board[j][i] == ".":
                    continue
                hm[board[j][i]] = 1 + hm.get(board[j][i], 0)
            for val in hm.values():
                if val > 1:
                    return False
        return True
    
    def checkBox(self, board: List[List[str]]):
        # boxes = [defaultdict(list)] * 9
        
        # board[0 + offset1 :3 + offset2 , 0 + offset1: 3 + offset2]
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                hm = defaultdict(list)
                for boxIdx1 in range(3):
                    for boxIdx2 in range(3):
                        if board[i + boxIdx1][j + boxIdx2] == ".":
                            continue
                        hm[board[i + boxIdx1][j + boxIdx2]] = 1 + hm.get(board[i + boxIdx1][j + boxIdx2], 0)
                for val in hm.values():
                    if val > 1:
                        return False
        return True

                




                
