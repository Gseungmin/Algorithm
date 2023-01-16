import sys
input = sys.stdin.readline
from collections import deque
N, M, K = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = []
Min = 10**6
Max = 0
for y in range(M):
    queue.append([graph[0][y],0,y])
    Min = min(Min, graph[0][y])
    Max = max(Max, graph[0][y])
    
for x in range(1,N):
    queue.append([graph[x][0],x,0])
    queue.append([graph[x][M-1],x,M-1])
    Min = min(Min, graph[x][0], graph[x][M-1])
    Max = max(Max, graph[x][0], graph[x][M-1])


left = 0
right = 10**6
ans = 0
while left <= right:
    mid = (left+right)//2
    new_true = [[False]*M for i in range(N)]
    new_heap = deque()
    for k, x, y in queue:
        if k <= mid:
            new_heap.append([k,x,y])
            new_true[x][y] = True
    cnt = len(new_heap)
    while new_heap:
        k, x, y = new_heap.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if new_true[nx][ny] == False:
                    if graph[nx][ny] <= mid:
                        cnt += 1
                        new_true[nx][ny] = True
                        new_heap.append([graph[nx][ny],nx,ny])
        if cnt >= K:
            break
    if cnt >= K:
        right = mid-1
        ans = mid
    else:
        left = mid+1
print(ans)