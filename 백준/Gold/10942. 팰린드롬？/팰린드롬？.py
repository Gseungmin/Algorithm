import sys
input = sys.stdin.readline
N = int(input())
graph = list(map(int,input().split()))
true = [[0]*N for i in range(N)]
for i in range(N):
    true[i][i] = 1
Len = 2
while Len <= N:
    for i in range(N):
        j = i+Len-1
        if j >= N:
            break
        if Len%2 != 0:
            if true[i+1][j-1] == 1 and graph[i] == graph[j]:
                true[i][j] = 1
        else:
            if Len == 2:
                if graph[i] == graph[j]:
                    true[i][j] = 1
            else:
                if graph[i] == graph[j] and true[i+1][j-1] == 1:
                    true[i][j] = 1
    Len += 1
M = int(input())
for i in range(M):
    a, b = map(int,input().split())
    print(true[a-1][b-1])