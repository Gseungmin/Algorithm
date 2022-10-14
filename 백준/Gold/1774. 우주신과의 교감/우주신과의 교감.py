import sys
input = sys.stdin.readline
N, M = map(int,input().split())
List = [[]]
for i in range(N):
    List.append(list(map(int,input().split())))
import heapq
import math
heap = []
for i in range(1,N):
    for j in range(i+1,N+1):
        cost = math.dist(List[i],List[j])
        heapq.heappush(heap, [cost,i,j])
UF = [i for i in range(N+1)]
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
for i in range(M):
    x, y = map(int,input().split())
    Union(x,y)
ans = 0
while heap:
    c, x, y = heapq.heappop(heap)
    a = Find(x)
    b = Find(y)
    if a == b or Find(a) == b or Find(b) == a or Find(a) == Find(b):
        continue
    ans += c
    Union(a,b)
print("{:.2f}".format(ans))