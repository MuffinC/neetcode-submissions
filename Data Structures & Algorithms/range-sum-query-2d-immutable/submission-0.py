class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r,c=len(matrix), len(matrix[0])
        self.mats=[[] for _ in range(r)]
        #mats containe prefix values for the 2d matrix in rows
        for z in range(r):
            for y in range(c):
                if y==0:
                    self.mats[z].append(matrix[z][y])
                else: self.mats[z].append(self.mats[z][y-1]+matrix[z][y])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=0
        for x in range(row1,row2+1):
            #we only need the start to tell what to minus and end of each row for prefix
            if col1==0:
                ans+=self.mats[x][col2]
            else:
                ans+=(self.mats[x][col2] - self.mats[x][col1 -1])

        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)