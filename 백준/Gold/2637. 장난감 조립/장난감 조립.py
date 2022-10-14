import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
cost = dict()
graph = [[] for i in range(N+1)]
ind = [0]*(N+1)
ind_r = [0]*(N+1)
true = [-1]*(N+1)
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    cost[(a,b)] = c
    ind_r[a] += 1
    ind[b] += 1
arr = []
for i in range(1,N+1):
    if ind_r[i] == 0:
        arr.append(i)
cnt = [0]*(N+1)
from collections import deque
queue = deque()
queue.append(N)
cnt[N] = 1
true[N] = 0
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if true[nx] == -1:
            cnt[nx] += cnt[x]*cost[(x,nx)]
            ind[nx] -= 1
            if ind[nx] == 0:
                true[nx] = 0
                queue.append(nx)
for i in arr:
    print(i, cnt[i])