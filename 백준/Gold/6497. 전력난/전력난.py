import sys
input = sys.stdin.readline
import heapq

def Find(x):
    if x == UF[x]:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y
def Union(x,y):
    a = Find(x)
    b = Find(y)
    if a == b:
        return
    elif a > b:
        UF[a] = b
    elif a < b:
        UF[b] = a
    return

while 1:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    ans = 0
    UF = [i for i in range(N)]
    heap = []
    for i in range(M):
        a, b, c = map(int,input().split())
        ans += c
        heapq.heappush(heap,[c,a,b])
    while heap:
        t, x, y = heapq.heappop(heap)
        if Find(x) == Find(y):
            continue
        ans -= t
        Union(x,y)
    print(ans)