import sys
input = sys.stdin.readline
N, P = map(int,input().split())
city = [0]*(N+1)
city[0] = int(1e9)
for i in range(1,N+1):
    k = int(input())
    city[i] = k
import heapq
heap = []
graph = dict()
for i in range(P):
    a, b, c = map(int,input().split())
    graph[(a,b)] = c
    graph[(b,a)] = c
    heapq.heappush(heap,[c+city[b]+c+city[a],a,b])

UF = [i for i in range(N+1)]
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
while heap:
    t, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    Union(X,Y)
    ans += t

print(ans+min(city))