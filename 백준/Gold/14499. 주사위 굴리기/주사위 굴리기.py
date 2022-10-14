import sys
input = sys.stdin.readline
N, M, x, y, K = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
move = list(map(int,input().split()))
up = 1
down = 6
east = 3
west = 4 
front = 5
back = 2
Dict = dict()
Dict[up] = 0
Dict[down] = 0
Dict[east] = 0
Dict[west] = 0
Dict[front] = 0
Dict[back] = 0
for i in move:
    if i == 1:
        nx, ny = x, y+1
        if ny == M:
            continue
        up, east, down, west = west, up, east, down
        if graph[nx][ny] == 0:
            graph[nx][ny] = Dict[down]
        else:
            Dict[down] = graph[nx][ny]
            graph[nx][ny] = 0
        print(Dict[up])
        x, y = nx, ny
    if i == 2:
        nx, ny = x, y-1
        if ny == -1:
            continue
        up, east, down, west = east, down, west, up
        if graph[nx][ny] == 0:
            graph[nx][ny] = Dict[down]
        else:
            Dict[down] = graph[nx][ny]
            graph[nx][ny] = 0
        print(Dict[up])
        x, y = nx, ny
    if i == 3:
        nx, ny = x-1, y
        if nx == -1:
            continue
        up, front, down, back = front, down, back, up
        if graph[nx][ny] == 0:
            graph[nx][ny] = Dict[down]
        else:
            Dict[down] = graph[nx][ny]
            graph[nx][ny] = 0
        print(Dict[up])
        x, y = nx, ny
    if i == 4:
        nx, ny = x+1, y
        if nx == N:
            continue
        up, front, down, back = back, up, front, down
        if graph[nx][ny] == 0:
            graph[nx][ny] = Dict[down]
        else:
            Dict[down] = graph[nx][ny]
            graph[nx][ny] = 0
        print(Dict[up])
        x, y = nx, ny