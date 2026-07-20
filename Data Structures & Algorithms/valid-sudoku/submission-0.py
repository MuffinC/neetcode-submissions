class Solution:
    def sqs(self,x,y,board):
        seensq=set()
        for z in range(x,x+3,1):
            for g in range(y,y+3,1):
                if board[g][z] !="." and board[g][z] not in seensq: seensq.add(board[g][z])
                elif board[g][z] =='.': continue
                else: return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        n=len(board)
        for x in range(n):  
            seenrow=set()
            for y in range(n):
                if board[x][y] !="." and board[x][y] not in seenrow: seenrow.add(board[x][y])
                elif board[x][y] =='.': continue
                else: return False
 
        #col check
        for x in range(n):  
            seencol=set()
            for y in range(n):
                if board[y][x] !="." and board[y][x] not in seencol: seencol.add(board[y][x])
                elif board[y][x] =='.': continue
                else: return False

        #square check 
        for x in range(0,n,3):  
            for y in range(0,n,3):
                if self.sqs(x,y,board): continue
                else: return False

        return True

    