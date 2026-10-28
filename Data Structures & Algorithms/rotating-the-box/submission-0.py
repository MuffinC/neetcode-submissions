class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        l,w=len(boxGrid), len(boxGrid[0])
        
        for x in range(l):
            empt=[]
            for y in range(w-1,-1,-1):
                if boxGrid[x][y]=='.':
                   empt.append((x,y))
                elif  boxGrid[x][y]=='*':
                    empt=[]
                elif boxGrid[x][y]=='#'and empt:
                    dx,dy=empt.pop(0)
                    boxGrid[dx][dy]=boxGrid[x][y]
                    boxGrid[x][y]='.'
                    empt.append((x,y))

        #now rotate boxgrid and return


        return [list(row) for row in zip(*boxGrid[::-1])]
                
