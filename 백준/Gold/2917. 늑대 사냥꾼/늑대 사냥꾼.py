import sys
input = sys.stdin.readline
import heapq
from collections import deque

#입력조건 초기화
N, M = map(int,input().split())
graph = [list(input().rstrip()) for i in range(N)]

#트리 위치 및 현재 초기화
tree = []
x, y = 0, 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "+": #트리 위치 초기화
            tree.append([i,j])
        elif graph[i][j] == "V": #현재 위치 초기화
            x, y = i, j

dx = [-1,1,0,0]
dy = [0,0,-1,1]

INF = int(1e9)

#트리와 거리 초기화
queue_true = [[False]*M for i in range(N)]
dist = [[INF]*M for i in range(N)]

queue = deque()
for i, j in tree:
    dist[i][j] = 0
    queue.append([i,j])
    queue_true[i][j] = True

while queue:
    i, j = queue.popleft()
    for m in range(4):
        ni, nj = i+dx[m], j+dy[m]
        if 0<=ni<N and 0<=nj<M:
            if queue_true[ni][nj] == False:
                queue_true[ni][nj] = True
                dist[ni][nj] = dist[i][j]+1
                queue.append([ni,nj])

#다익스트라 초기화
true = [[False]*M for i in range(N)]
heap = [[-dist[x][y],x,y]]

#다익스트라
while heap:
    k, x, y = heapq.heappop(heap)
    k = -k
    if true[x][y] == True:
        continue
    true[x][y] = True
    if graph[x][y] == "J":
        print(k)
        sys.exit()
    for m in range(4):
        nx, ny = x + dx[m], y + dy[m]
        if 0<=nx<N and 0<=ny<M:
            if true[nx][ny] == False:
                if dist[nx][ny] >= dist[x][y]: #이동하려는 곳이 나무와 거리가 더 먼 경우
                    dist[nx][ny] = dist[x][y]
                    heapq.heappush(heap,[-dist[nx][ny], nx, ny])
                elif dist[nx][ny] < dist[x][y]: #이동하려는 곳보다 현재가 더 먼 경우
                    heapq.heappush(heap,[-dist[nx][ny], nx, ny])