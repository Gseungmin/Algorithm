import sys
input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
Length = 21
parent = [[0]*Length for i in range(N+1)]
from collections import deque
queue = deque()
queue.append(1)
level = [-1]*(N+1)
level[1] = 0
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if level[nx] == -1:
            level[nx] = level[x] + 1
            parent[nx][0] = x
            queue.append(nx)

for j in range(1,Length):
    for i in range(1,N+1):
        if parent[i][j-1] >= 0:
            parent[i][j] = parent[parent[i][j-1]][j-1]

def lca(a,b):
    if level[a] > level[b]:
        a, b = b, a
    for i in range(Length-1,-1,-1):
        if level[b]-level[a] >= (1<<i):
            b = parent[b][i]
    if a == b:
        return a
    for i in range(Length-1,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

M = int(input())
ans = 0
List = [1]
for i in range(M):
    num = int(input())
    List.append(num)
for i in range(len(List)-1):
    left = List[i]
    right = List[i+1]
    k = lca(left,right)
    ans += (level[left]+level[right]-level[k]*2)
print(ans)