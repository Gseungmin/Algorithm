import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
Max = graph[0][0]
for i in range(N):
    for j in range(N):
        Max = max(Max, graph[i][j])
S = [[0]*N for i in range(N)]
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

size = 2
while size <= N:
    for i in range(N-size+1):
        for j in range(N-size+1):
            a, b, x, y = i, j, i+size-1, j+size-1
            if a-1>=0 and b-1>=0:
                value = S[x][y] - S[a-1][y] - S[x][b-1] + S[a-1][b-1]
            elif a-1<0 and b-1>=0:
                value = S[x][y] - S[x][b-1]
            elif a-1>=0 and b-1<0:
                value = S[x][y] - S[a-1][y]
            else:
                value = S[x][y]
            Max = max(Max, value)
    size += 1
print(Max)