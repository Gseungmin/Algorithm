import sys
input = sys.stdin.readline
N = int(input())
Length = 21
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b, c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
level = [-1]*(N+1)
from collections import deque
queue = deque()
queue.append(1)
p = [[0]*(Length) for i in range(N+1)]
dist = [-1]*(N+1)
level[1] = 0
dist[1] = 0
while queue:
    x = queue.popleft()
    for nx, k in graph[x]:
        if level[nx] == -1:
            p[nx][0] = x
            level[nx] = level[x] + 1
            dist[nx] = dist[x] + k
            queue.append(nx)

for i in range(1,Length):
    for j in range(1,N+1):
        if p[j][i-1] != 0:
            p[j][i] = p[p[j][i-1]][i-1]

def lca(a, b):
    if level[a] > level[b]:
        a, b = b, a
    for i in range(Length-1,-1,-1):
        if level[b]-level[a] >= (1<<i):
            b = p[b][i]
    if a == b:
        return a
    for i in range(Length-1,-1,-1):
        if p[a][i] != p[b][i]:
            a = p[a][i]
            b = p[b][i]
    return p[a][0]

M = int(input())
for i in range(M):
    a, b = map(int,input().split())
    print(dist[a]+dist[b]-2*dist[lca(a,b)])