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
arr = [list(input().strip()) for i in range(N)]
Dict = dict()
for i in range(97,123):
    Dict[chr(i)] = i-96
for i in range(65,91):
    Dict[chr(i)] = i-64+26
UF = [i for i in range(N)]
import heapq
heap = []
All = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == "0":
            continue
        All += Dict[arr[i][j]]
        if i == j:
            continue
        heapq.heappush(heap,[Dict[arr[i][j]],i,j])
if N == 1:
    print(All)
    sys.exit()
value = 0
while heap:
    t, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    value += t
    Union(x,y)
for i in range(1,N):
    if i == UF[i]:
        print(-1)
        sys.exit()
print(All-value)