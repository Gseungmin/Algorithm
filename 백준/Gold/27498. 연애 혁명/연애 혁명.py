import sys
input = sys.stdin.readline
import heapq

#5:27
#사랑관계를 포기하도록 해야함
#이미 성사된 사랑관계는 포기 x
#사랑관계에 사이클이 있으면 안됨
#포기하도록 만든 애정도의 합 최소

N, M = map(int,input().split())

heap = []

for i in range(M):
    a, b, c, d = map(int,input().split())
    heapq.heappush(heap,[-d,-c,a-1,b-1])

UF = [i for i in range(N)]

def Find(x):
    if UF[x] == x:
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

ans = 0
while heap:
    d, c, a, b = heapq.heappop(heap)
    
    if d == -1:
        Union(a,b)
        continue
    
    X = Find(a)
    Y = Find(b)
    
    if X == Y:
        ans += -c
        continue
    
    Union(X,Y)

print(ans)