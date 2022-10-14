import sys
input = sys.stdin.readline
N, M = map(int,input().split())
true = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    true[a][b] = 1
    true[b][a] = 1

if N < 3:
    print(0)
    sys.exit()
List = []

cnt = 0
for i in range(1,N-1):
    for j in range(i+1,N):
        for k in range(j+1,N+1):
            if true[i][j] == 0 and true[i][k] == 0 and true[j][k] == 0:
                cnt += 1
print(cnt)