#https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem

def getBiggestRegion(grid):
    height = len(grid)
    width = len(grid[0])
    record = 0
    
    for h in range(height):
        for w in range(width):
            if grid[h][w]:
                record = max(record, DFS(grid,h,w))
    return record
    
def DFS(grid,y,x):
    height = len(grid)
    width = len(grid[0])
    count = 1
    grid[y][x] = 0
    
    adjacents = [
        [y+1, x-1],
        [y+1, x  ],
        [y+1, x+1],
        [y  , x-1],
        [y  , x+1],
        [y-1, x-1],
        [y-1, x  ],
        [y-1, x+1],
    ]
    
    for adj in adjacents:
        if (adj[0] < height and adj[0] >= 0) and (adj[1] < width and adj[1] >= 0):
            h = adj[0]
            w = adj[1]
            if grid[h][w]:
                count += DFS(grid, h, w)
    return count

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
