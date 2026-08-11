class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 0:
                    q.append((x, y))
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 2147483647:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))
