def Find(x):
    if x == UF[x]:
        return x
    y = Find(UF[x])
    UF[x] = Find(y)
    return y

def Union(x,y):
    X = Find(x)
    Y = Find(y)
    if X == Y:
        return
    if X > Y:
        UF[X] = Y
    else:
        UF[Y] = X
    return

N, M = map(int,input().split())
graph = [list(input()) for i in range(N)]
arr = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == "S" or graph[i][j] == "K":
            arr.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque
INF = int(1e9)
def BFS(a,b,true,dist):
    queue = deque()
    queue.append([a,b])
    true[a][b] = True
    dist[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if true[nx][ny] == False and graph[nx][ny] != "1":
                    true[nx][ny] = True
                    queue.append([nx,ny])
                    dist[nx][ny] = dist[x][y] + 1
    return

import heapq
heap = []
for i in range(len(arr)-1):
    sx, sy = arr[i]
    true = [[False]*N for i in range(N)]
    dist = [[INF]*N for i in range(N)]
    BFS(sx,sy,true,dist)
    for j in range(i+1, len(arr)):
        if i == j:
            continue
        ex, ey = arr[j]
        if dist[ex][ey] == INF:
            print(-1)
            exit()
        heapq.heappush(heap,[dist[ex][ey],i,j])
UF = [i for i in range(len(arr))]
cnt = set()
ans = 0
while heap:
    k, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    Union(x,y)
    ans += k
    cnt.add(x)
    cnt.add(y)
if len(cnt) == len(arr):
    print(ans)
else:
    print(-1)