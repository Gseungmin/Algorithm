import sys
input = sys.stdin.readline
N, M, T = map(int,input().split())

import heapq
heap = []
for i in range(M):
    a, b, c = map(int,input().split())
    heapq.heappush(heap,[c,a,b])

UF = [i for i in range(N+1)]

def Union(x,y):
    X = Find(x)
    Y = Find(y)
    if X == Y:
        return
    if X > Y:
        UF[X] = Y
    else:
        UF[Y] = X
    return

def Find(x):
    if UF[x] == x:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y

ans = 0
edge = []
while heap:
    c, a, b = heapq.heappop(heap)
    A = Find(a)
    B = Find(b)
    if A == B:
        continue
    edge.append([a,b])
    Union(a,b)
    ans += c
    
graph = [[] for i in range(N+1)]
for x, y in edge:
    graph[x].append(y)
    graph[y].append(x)

true = [False]*(N+1)

from collections import deque
queue = deque()
queue.append(1)
true[1] = True
cnt = 0
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if true[nx] == False:
            ans += cnt*T
            queue.append(nx)
            true[nx] = True
            cnt += 1
        
print(ans)