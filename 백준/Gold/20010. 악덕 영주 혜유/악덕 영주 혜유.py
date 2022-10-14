import sys
input = sys.stdin.readline
import heapq
N, K = map(int,input().split())
heap = []
for i in range(K):
    a, b, c = map(int,input().split())
    heapq.heappush(heap,[c,a,b])

UF = [i for i in range(N)]
def Find(x):
    if x == UF[x]:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y

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

ans = 0
graph = [[] for i in range(N)]
while heap:
    k, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    Union(x,y)
    ans += k
    graph[x].append([y,k])
    graph[y].append([x,k])
Max = [0]
def DFS(x,prev,k):
    Max[0] = max(Max[0], k)
    for nx, c in graph[x]:
        if nx == prev:
            continue
        DFS(nx,x,k+c)
    return
for i in range(N):
    DFS(i,-1,0)
print(ans)
print(Max[0])