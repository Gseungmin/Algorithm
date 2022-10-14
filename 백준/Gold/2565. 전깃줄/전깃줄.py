import sys
input = sys.stdin.readline
N = int(input())
List = [list(map(int,input().split())) for i in range(N)]
List.sort()
dp = [1]*N
for i in range(N):
    for j in range(i):
        if List[i][1] > List[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(N-max(dp))