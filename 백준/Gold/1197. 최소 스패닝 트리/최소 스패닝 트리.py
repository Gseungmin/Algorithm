import sys
input = sys.stdin.readline
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

N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
import heapq
List = []
for i in range(M):
    a,b,c = map(int,input().split())
    heapq.heappush(List,[c,a,b])

UF = [i for i in range(N+1)]
ans = 0
while List:
    k,x,y = heapq.heappop(List)
    if Find(x) == Find(y) or Find(Find(x)) == Find(y) or Find(x) == Find(Find(y)):
        continue
    ans += k
    Union(x,y)
print(ans)