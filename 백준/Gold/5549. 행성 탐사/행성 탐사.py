import sys
input = sys.stdin.readline
N, M = map(int,input().split())
K = int(input())
graph = [list(input()) for i in range(N)]

change = dict()
change["J"] = 0
change["O"] = 1
change["I"] = 2

info = [[[0]*3 for i in range(M)] for j in range(N)]

info[0][0][change[graph[0][0]]] += 1

for i in range(1,M):
    for j in range(3):
        info[0][i][j] = info[0][i-1][j]
    info[0][i][change[graph[0][i]]] += 1

for i in range(1,N):
    for j in range(3):
        info[i][0][j] = info[i-1][0][j]
    info[i][0][change[graph[i][0]]] += 1

for i in range(1,N):
    for j in range(1,M):
        for k in range(3):
            info[i][j][k] = info[i-1][j][k] + info[i][j-1][k] - info[i-1][j-1][k]
        info[i][j][change[graph[i][j]]] += 1
    
for i in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    List = [0,0,0]
    for i in range(3):
        if x1 != 0 and y1 != 0:
            List[i] = info[x2][y2][i] - info[x1-1][y2][i] - info[x2][y1-1][i] + info[x1-1][y1-1][i]
        elif x1 != 0 and y1 == 0:
            List[i] = info[x2][y2][i] - info[x1-1][y2][i]
        elif x1 == 0 and y1 != 0:
            List[i] = info[x2][y2][i] - info[x2][y1-1][i]
        else:
            List[i] = info[x2][y2][i]
    for k in List:
        print(k, end = ' ')
    print()