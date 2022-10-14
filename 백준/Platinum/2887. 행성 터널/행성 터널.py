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
    elif a < b:
        UF[b] = a
    elif a > b:
        UF[a] = b
    return

N = int(input())
UF = [i for i in range(N+1)]
X = []
Y = []
Z = []
heap = []
Max = 0
for i in range(N):
    a, b, c = map(int,input().split())
    X.append([a,i])
    Y.append([b,i])
    Z.append([c,i])
X.sort()
Y.sort()
Z.sort()
for i in range(N-1):
    heapq.heappush(heap,[X[i+1][0]-X[i][0], X[i+1][1], X[i][1]])
    heapq.heappush(heap,[Y[i+1][0]-Y[i][0], Y[i+1][1], Y[i][1]])
    heapq.heappush(heap,[Z[i+1][0]-Z[i][0], Z[i+1][1], Z[i][1]])

ans = 0
while heap:
    t, x, y = heapq.heappop(heap)
    if Find(x) == Find(y):
        continue
    Union(x,y)
    ans += t
print(ans)