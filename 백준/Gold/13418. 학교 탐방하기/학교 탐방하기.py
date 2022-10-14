import sys
input = sys.stdin.readline
N, M = map(int,input().split())

def Union(x, y, UF):
    X = Find(x, UF)
    Y = Find(y, UF)
    if X == Y:
        return
    if X > Y:
        UF[X] = Y
    elif X < Y:
        UF[Y] = X
    return

def Find(x, UF):
    if x == UF[x]:
        return x
    y = Find(UF[x],UF)
    UF[x] = y
    return y

import heapq
max_heap = []
min_heap = []
max_uf = [i for i in range(N+1)]
min_uf = [i for i in range(N+1)]

k = list(map(int,input().split()))
for i in range(M):
    a, b, c = map(int,input().split())
    c = 1-c
    heapq.heappush(max_heap,[-c,a,b])
    heapq.heappush(min_heap,[c,a,b])

m = k[2]
m = 1-m
Union(0,1,min_uf)
Min = m
check = 1
while min_heap:
    t, x, y = heapq.heappop(min_heap)
    X = Find(x, min_uf)
    Y = Find(y, min_uf)
    if X == Y:
        continue
    check += 1
    Min += t
    if check == N:
        break
    Union(X, Y, min_uf)

Max = m
check = 1
Union(0,1,max_uf)
while max_heap:
    t, x, y = heapq.heappop(max_heap)
    X = Find(x, max_uf)
    Y = Find(y, max_uf)
    if X == Y:
        continue
    check += 1
    Max += -t
    if check == N:
        break
    Union(X, Y, max_uf)

print((Max)**2-(Min)**2)