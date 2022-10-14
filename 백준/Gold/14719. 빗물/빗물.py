import sys
input = sys.stdin.readline
N, M = map(int,input().split())
List = list(map(int,input().split()))
graph = [[0]*M for i in range(N)]
if M == 1:
    print(0)
    sys.exit()
for i in range(M):
    for j in range(List[i]):
        graph[j][i] = 1
cnt = 0
for i in range(N):
    x = 0
    k = 1
    while x < M:
        while x < M and graph[i][x] != 1:
            x += 1
        if x == M-1:
            break
        k = x+1
        if k >= M:
            break
        if graph[i][k] == 1:
            x = k
            continue
        while k < M and graph[i][k] != 1:
            k += 1
        if k >= M:
            break
        if graph[i][k] == 0:
            continue
        cnt += (k-x-1)
        x = k
print(cnt)