import sys
input = sys.stdin.readline
from collections import deque

def BFS(graph, x, y, dx, dy, true, queue, ans):
    true[x][y] = 1
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if (0<=a<N) and (0<=b<M):
            if graph[a][b] == 0 and true[a][b] == 0:
                true[a][b] = 1
                queue.append([a,b])
                ans[a][b] = ans[x][y] + 1
                true[-1][0] = max(true[-1][0], ans[a][b])
    return

M, N = map(int,input().split())
graph = []
true = []
ans = []
for i in range(N):
    graph.append(list(map(int,input().split())))
    true.append([0]*M)
    ans.append([0]*M)
true.append([0])
queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i,j])
dx = [-1,1,0,0]
dy = [0,0,1,-1]
while queue:
    x, y = queue.popleft()
    BFS(graph, x, y, dx, dy, true, queue, ans)
    
for i in range(N):
    for j in range(M):
        if true[i][j] == 0 and graph[i][j] != -1:
            print(-1)
            sys.exit()
print(true[-1][0])