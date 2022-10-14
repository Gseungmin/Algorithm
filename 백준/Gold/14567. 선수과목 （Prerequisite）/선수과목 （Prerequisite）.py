import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
ind = [0]*(N+1)
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    ind[b] += 1
Class = [0]*(N+1)
from collections import deque
queue = deque()
true = [False]*(N+1)
for i in range(1,N+1):
    if ind[i] == 0:
        true[i] = True
        Class[i] = 1
        queue.append([i,1])
while queue:
    x, t = queue.popleft()
    for nx in graph[x]:
        if true[nx] == False:
            ind[nx] -= 1
            if ind[nx] == 0:
                true[nx] = True
                Class[nx] = t+1
                queue.append([nx,t+1])
print(" ".join(map(str,Class[1:])))