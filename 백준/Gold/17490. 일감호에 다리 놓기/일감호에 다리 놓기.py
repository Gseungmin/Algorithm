import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N, M, K = map(int,input().split()) #강의동 수, 공사 구간 수, 돌의 수
List = [0] + list(map(int,input().split()))

UF = [i for i in range(N+1)]

if M <= 1:
    print("YES")
    sys.exit()

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

impos = dict()
for i in range(M):
    a, b = map(int,input().split())
    impos[(a,b)] = True
    
import heapq
heap = []
for i in range(1,N+1):
    n = i+1
    if i == N:
        n = 1
    if (i,n) in impos or (n,i) in impos:
        continue
    else:
        Union(n,i)
        
for i in range(1,N+1):
    heapq.heappush(heap, [List[i], 0, i])

ans = 0
while heap:
    k, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    Union(X, Y)
    ans += k

if ans > K:
    print("NO")
else:
    print("YES")