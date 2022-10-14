import sys
input = sys.stdin.readline
N = int(input())
Length = 21
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [-1]*(N+1)
level = [0]*(N+1)
from collections import deque
queue = deque()
queue.append(1)
parent[1] = 0
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if parent[nx] == -1:
            parent[nx] = x
            level[nx] = level[x] + 1
            queue.append(nx)

p = [[0]*(Length) for i in range(N+1)]
for i in range(1,N+1):
    p[i][0] = parent[i]
for i in range(1,Length):
    for j in range(1,N+1):
        if p[j][i-1] != 0:
            p[j][i] = p[p[j][i-1]][i-1]

def lca(a, b):
    if level[a] > level[b]:
        a, b = b, a
    for i in range(Length-1,-1,-1):
        if level[b]-level[a] >= 2**i:
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
    print(lca(a,b))