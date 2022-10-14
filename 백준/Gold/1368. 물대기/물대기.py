import sys
input = sys.stdin.readline

def Union(x, y):
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

N = int(input())
List = [int(input()) for i in range(N)]
graph = [list(map(int,input().split())) for i in range(N)]
import heapq
heap = []
for i in range(N):
    for j in range(i+1,N):
        if i == j:
            continue
        heapq.heappush(heap,[graph[i][j],i,j])

for i in range(N):
    heapq.heappush(heap,[List[i], i, N])

ans = 0
UF = [i for i in range(N+1)]
while heap:
    t, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    Union(X,Y)
    ans += t
print(ans)