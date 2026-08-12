class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        arr=[]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        import heapq
        heapq.heapify(arr)
        r,c=len(grid),len(grid[0])
        for x in range(r):
            for y in range(c):
                if grid[x][y]==2:
                    heapq.heappush(arr,tuple((0,x,y)))

        ans=0
        seen=set()
        while arr:
            d,x,y=heapq.heappop(arr)
            ans=max(ans, d)
            for rx,ry in directions:
                dx,dy=rx+x, ry+y
                if dx<0 or dy<0 or dx>=r or dy >=c or tuple((dx,dy)) in seen or grid[dx][dy]!=1: continue
                seen.add(tuple((dx,dy)))
                grid[dx][dy]=2
                heapq.heappush(arr, tuple((d+1,dx,dy)))
        for x in range(r):
            for y in range(c):
                if grid[x][y]==1: return -1
        return ans