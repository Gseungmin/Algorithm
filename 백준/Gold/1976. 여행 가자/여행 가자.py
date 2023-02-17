#12/45
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

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
    if X > Y:
        UF[X] = Y
    elif X < Y:
        UF[Y] = X
    return

k = []
graph = [list(map(int,input().split())) for i in range(N)]

List = list(map(int,input().split()))
for i in range(len(List)):
    List[i] -= 1
    
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            x = Find(i)
            y = Find(j)
            if x == y:
                continue
            Union(x,y)

a = Find(List[0])
check = True
for i in range(1,M):
    if a != Find(List[i]):
        check = False
        break

if check == False:
    print("NO")
else:
    print("YES")