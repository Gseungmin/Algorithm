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
    if UF[x] == x:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
UF = [i for i in range(N)]
for i in range(M):
    a, b = map(int,input().split())
    Union(a-1,b-1)
cost = [list(map(int,input().split())) for i in range(N)]
import heapq
heap = []
for i in range(1,N):
    for j in range(i+1,N):
        heapq.heappush(heap,[cost[i][j],i,j])
cnt = 0
value = 0
List = []
while heap:
    t, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    cnt += 1
    value += t
    List.append([x,y])
    Union(X,Y)
print(value, cnt)
for a, b in List:
    print(a+1, b+1)