import sys
input = sys.stdin.readline

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

N = int(input())
ans = dict()
for i in range(1,N+1):
    ans[i] = []
import heapq
heap = []
for i in range(1,N+1):
    List = list(map(int,input().split()))
    j = i+1
    for k in List:
        heapq.heappush(heap,[k,i,j])
        j += 1
UF = [i for i in range(N+1)]
while heap:
    k, a, b = heapq.heappop(heap)
    x = Find(a)
    y = Find(b)
    if x == y:
        continue
    Union(x,y)
    ans[a].append(b)
    ans[b].append(a)
for i in range(1,N+1):
    L = len(ans[i])
    ans[i].sort()
    print(L, end = " ")
    for j in ans[i]:
        print(j, end = " ")
    print()