import sys
input = sys.stdin.readline
N, M = map(int,input().split())
S = [[0]*N for i in range(N)]
graph = [list(map(int,input().split())) for i in range(N)]
value = 0
for i in range(N):
    value += graph[0][i]
    S[0][i] = value
value = 0
for i in range(N):
    value += graph[i][0]
    S[i][0] = value
for i in range(1,N):
    for j in range(1,N):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + graph[i][j]
for i in range(M):
    a,b,x,y = map(int,input().split())
    a,b,x,y = a-1,b-1,x-1,y-1
    if a-1 >= 0 and b-1 >= 0:
        print(S[x][y]-S[x][b-1]-S[a-1][y]+S[a-1][b-1])
    elif a-1 >= 0 and b-1 < 0:
        print(S[x][y]-S[a-1][y])
    elif b-1 >= 0 and a-1 < 0:
        print(S[x][y]-S[x][b-1])
    else:
        print(S[x][y])