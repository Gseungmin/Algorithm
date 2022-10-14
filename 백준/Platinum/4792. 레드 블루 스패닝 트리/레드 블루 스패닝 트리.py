import sys
input = sys.stdin.readline

def Find(x):
    if x == UF[x]:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y

def Union(x, y):
    X = Find(x)
    Y = Find(y)
    if X == Y:
        return
    if X > Y:
        UF[X] = Y
    elif X < Y:
        UF[Y] = X
    return

def MST(heap):
    cnt = 0
    while heap:
        k, x, y = heapq.heappop(heap)
        X = Find(x)
        Y = Find(y)
        if X == Y:
            continue
        if k == 0:
            cnt += 1
        Union(x,y)
    ans.append(cnt)
    return 
    
import heapq
while 1:
    N, M, K = map(int,input().split())
    if N == 0 and M == 0 and K == 0:
        break
    heapB = []
    heapR = []
    for i in range(M):
        a, b, c = map(str,input().split())
        if a == "B":
            heapq.heappush(heapB,[0,int(b), int(c)])
            heapq.heappush(heapR,[0,int(b), int(c)])
        else:
            heapq.heappush(heapB,[1,int(b), int(c)])
            heapq.heappush(heapR,[-1,int(b), int(c)])
    heap = [heapB, heapR]
    ans = []
    for i in range(2):
        UF = [v for v in range(N+1)]
        MST(heap[i])
    ans.sort()
    if ans[0] <= K <= ans[1]:
        print(1)
    else:
        print(0)