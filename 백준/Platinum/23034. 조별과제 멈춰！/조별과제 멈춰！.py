import sys
input = sys.stdin.readline

def Union(x,y):
    X = Find(x)
    Y = Find(y)
    if X == Y:
        return
    if X > Y:
        UF[X] = Y
    elif X < Y:
        UF[Y] = X
    return

def Find(x):
    if x == UF[x]:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y

N, M = map(int,input().split())
import heapq
heap = []
for i in range(M):
    a, b, c = map(int,input().split())
    heapq.heappush(heap,[c,a,b])

UF = [i for i in range(N+1)]
ans = 0
graph = [[] for i in range(N+1)]
while heap:
    c, a, b = heapq.heappop(heap)
    x = Find(a)
    y = Find(b)
    if x == y:
        continue
    graph[a].append([b,c])
    graph[b].append([a,c])
    Union(x,y)
    ans += c

from collections import deque
INF = int(1e9)
Q = int(input())
for i in range(Q):
    a, b = map(int,input().split())
    true = [False]*(N+1)
    dist = [0]*(N+1)
    queue = deque()
    queue.append(a)
    while queue:
        x = queue.popleft()
        for nx, t in graph[x]:
            if true[nx] == False:
                true[nx] = True
                dist[nx] = max(dist[x], t)
                queue.append(nx)
        if true[b] == True:
            break
    print(ans-dist[b])