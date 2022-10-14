import sys
input = sys.stdin.readline
N, M, F = map(int,input().split())

def Union(x,y,UF):
    X = Find(x,UF)
    Y = Find(y,UF)
    if X == Y:
        return
    elif X > Y:
        UF[X] = Y
    elif Y > X:
        UF[Y] = X
    return

def Find(x,UF):
    if UF[x] == x:
        return x
    y = Find(UF[x],UF)
    UF[x] = y
    return y

import heapq
heap = []
List = [list(map(int,input().split())) for i in range(M)]
def MST():
    heap = []
    for i, j, c, t in List:
        heapq.heappush(heap,[c+mid*t,c,t,i,j])
    cost = 0
    time = 0
    UF = [i for i in range(N+1)]
    while heap:
        k, c, t, i, j = heapq.heappop(heap)
        x = Find(i,UF)
        y = Find(j,UF)
        if x == y:
            continue
        cost += c
        time += t
        Union(x,y,UF)
    if F-cost >= 0:
        return [True, round((F-cost)/time,4)]
    return False
ans = 0
left = 0
right = int(1e9)
for i in range(200):
    mid = (left+right)/2.0
    check = MST()
    if check == False:
        left = mid
    else:
        right = mid
        ans = max(ans,check[1])
ans = "{:.4f}".format(ans)
print(ans)