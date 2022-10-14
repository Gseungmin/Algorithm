import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
cost = dict()
ind = [0]*(N+1)
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    cost[(a,b)] = c
    ind[b] += 1

dist = [0]*(N+1)
true = [False]*(N+1)
parent = [0]*(N+1)
from collections import deque
queue = deque()
queue.append(1)
while queue:
    x = queue.popleft()
    if ind[1] == 0:
        break
    for nx in graph[x]:
        if true[nx] == False:
            ind[nx] -= 1
            if dist[nx] < dist[x]+cost[(x,nx)]:
                dist[nx] = dist[x]+cost[(x,nx)]
                parent[nx] = x
            if ind[nx] == 0:
                queue.append(nx)
                true[nx] = True
print(dist[1])
ans = []
i = 1
while 1:
    ans.append(i)
    i = parent[i]
    if i == 1:
        ans.append(i)
        break
ans.reverse()
print(" ".join(map(str,ans)))