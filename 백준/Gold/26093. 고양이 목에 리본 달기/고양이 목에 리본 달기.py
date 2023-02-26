import sys
input = sys.stdin.readline
N, K = map(int,input().split())

info = [list(map(int,input().split())) for i in range(N)]

if N == 1:
    print(max(info[0]))
    sys.exit()

index_max = dict()
for i in range(N):
    index_max[i] = []

#i번째 고양이한테 j리본 연결
dp = [[0]*K for i in range(N)]
for i in range(K):
    dp[0][i] = info[0][i]
    if len(index_max[0]) < 2:
        index_max[0].append([dp[0][i], i])
        index_max[0].sort(reverse = True)
    else:
        if index_max[0][-1][0] < dp[0][i]:
           index_max[0].pop()
           index_max[0].append([dp[0][i], i])
           index_max[0].sort(reverse = True)
           
for i in range(1,N):
    a, b = index_max[i-1][0]
    c, d = index_max[i-1][1]
    for j in range(K):
        if j != b:
            dp[i][j] = a + info[i][j]
        else:
            dp[i][j] = c + info[i][j]
            
        if len(index_max[i]) < 2:
            index_max[i].append([dp[i][j], j])
            index_max[i].sort(reverse = True)
        else:
            if index_max[i][-1][0] < dp[i][j]:
               index_max[i].pop()
               index_max[i].append([dp[i][j], j])
               index_max[i].sort(reverse = True)
            
ans = 0
for i in range(K):
    ans = max(ans,dp[N-1][i])

print(ans)