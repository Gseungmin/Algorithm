import sys
input = sys.stdin.readline
import heapq
N = int(input())
dist = [list(input().split()) for i in range(N)]
for i in range(N):
    for j in range(N):
        dist[i][j] = int(dist[i][j])

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
    elif Y > X:
        UF[Y] = X
    return

heap = []
ans = 0
Set = set()
for i in range(N):
    for j in range(N):
        if dist[i][j] < 0:
            Union(i,j)
            ans += (-dist[i][j])
            Set.add(i)
            Set.add(j)
        elif dist[i][j] > 0:
            heapq.heappush(heap,[dist[i][j], i, j])
ans //= 2
List = []
cnt = 0
while heap:
    k, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    Union(X, Y)
    List.append([x+1,y+1])
    ans += k
    cnt += 1
print(ans, cnt)
for x, y in List:
    print(x, y)