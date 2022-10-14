import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
cost = dict()
cost_r = dict()
graph = [[] for i in range(N+1)]
graph_r = [[] for i in range(N+1)]
ind = [0]*(N+1)
ind_r = [0]*(N+1)
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    graph_r[b].append(a)
    ind_r[a] += 1
    ind[b] += 1
    cost_r[(b,a)] = c
    cost[(a,b)] = c
s, e = map(int,input().split())
from collections import deque
queue = deque()
queue.append(s)
true = [False]*(N+1)
true[s] = True
dist = [-1]*(N+1)
dist[s] = 0
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if true[nx] == False:
            dist[nx] = max(dist[nx],dist[x]+cost[(x,nx)])
            ind[nx] -= 1
            if ind[nx] == 0:
                queue.append(nx)
                true[nx] = True

queue = deque()
true = [False]*(N+1)
queue.append(e)
true[e] = True
edge = 0
while queue:
    x = queue.popleft()
    for nx in graph_r[x]:
        if true[x] and cost_r[(x,nx)] == dist[x]-dist[nx]:
            edge += 1
            true[nx] = True
        ind_r[nx] -= 1
        if ind_r[nx] == 0:
            queue.append(nx)
print(dist[e])
print(edge)