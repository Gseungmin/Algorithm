import sys
input = sys.stdin.readline
N = int(input())
graph = [list(input().rstrip()) for i in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] != "#":
            graph[i][j] = int(graph[i][j])

#N이 2보다 작은 경우 처리
if N <= 2:
    print(0)
    sys.exit()

not_mine = dict()
mine = dict()

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

row_1 = [[0,i] for i in range(N-1)]

row_N = [[N-1,i] for i in range(N-1)]

col_1 = [[i,0] for i in range(N-1)]

col_N = [[i,N-1] for i in range(N-1)]

#N이 3보다 작은 경우 철리
for x, y in row_1:
    if graph[x][y] == 0:
        not_mine[(x+1,y+1)] = True
    elif graph[x][y] == 1:
        mine[(x+1,y+1)] = True
        if y+1 != N-1:
            graph[x][y+1] = max(graph[x][y+1]-1, 0)
        if y+2 != N-1:
            graph[x][y+2] = max(graph[x][y+2]-1, 0)

for x, y in row_N:
    if graph[x][y] == 0:
        not_mine[(x-1,y+1)] = True
    elif graph[x][y] == 1:
        mine[(x-1,y+1)] = True
        if y+1 != N-1:
            graph[x][y+1] = max(graph[x][y+1]-1, 0)
        if y+2 != N-1:
            graph[x][y+2] = max(graph[x][y+2]-1, 0)

for x, y in col_1:
    if graph[x][y] == 0:
        not_mine[(x+1,y+1)] = True
    elif graph[x][y] == 1:
        mine[(x+1,y+1)] = True
        if x+1 != N-1:
            graph[x+1][y] = max(graph[x+1][y]-1, 0)
        if x+2 != N-1:
            graph[x+2][y] = max(graph[x+2][y]-1, 0)

for x, y in col_N:
    if graph[x][y] == 0:
        not_mine[(x+1,y-1)] = True
    elif graph[x][y] <= 2:
        mine[(x+1,y-1)] = True
        if x+1 != N-1:
            graph[x+1][y] = max(graph[x+1][y]-1, 0)
        if x+2 != N-1:
            graph[x+2][y] = max(graph[x+2][y]-1, 0)

print(len(mine) + (max(N-4,0)*max(N-4,0)))