import sys
input = sys.stdin.readline
N, M, Q = map(int,input().split())
tank = list(map(int,input().split()))

UF = [i for i in range(N)]

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
    if X < Y:
        UF[Y] = X
    elif X > Y:
        UF[X] = Y
    return

for i in range(M):
    a, b = map(int,input().split())
    if UF[a-1] == UF[b-1]:
        continue
    Union(a-1,b-1)


connect = dict()
for i in range(N):
    UF[i] = Find(UF[i])
    if UF[i] not in connect:
        connect[UF[i]] = 0
        if tank[i] == 0:
            connect[UF[i]] -= 1
        else:
            connect[UF[i]] += 1
    else:
        if tank[i] == 0:
            connect[UF[i]] -= 1
        else:
            connect[UF[i]] += 1

for i in range(Q):
    k = int(input())
    if connect[UF[k-1]] > 0:
        print(1)
    else:
        print(0)