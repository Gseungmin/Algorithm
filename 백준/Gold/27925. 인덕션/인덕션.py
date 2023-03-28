#5:25

import sys
input = sys.stdin.readline

import heapq

#온도는 정수로 0~9사이
#첫 온도는 0, -,+를 누르면 1만큼 변동
#0에서 -는 9, 9에서 +는 0
#N개의 음식을 순서대로 요리, 각 음식에는 정확한 온도 필요
#온도 조절 횟수 최소
N = int(input())
arr = list(map(int,input().split()))

def dif(value, k):
    
    if value == k:
        cnt = 0
    elif value < k:
        cnt = min(k-value, value+9-k+1)
    else:
        cnt = min(9-value+1+k, value-k)
    return cnt

INF = int(1e9)
dp = [[[[INF]*10 for a in range(10)] for b in range(10)] for i in range(N)] #i 인덱스에서 a,b,c 온도를 가짐
cnt = dif(0,arr[0])

#dp 초기화
dp[0][arr[0]][0][0] = cnt
dp[0][0][arr[0]][0] = cnt
dp[0][0][0][arr[0]] = cnt

for i in range(N-1):
    value = arr[i+1]
    for a in range(10):
        for b in range(10):
            for c in range(10):
                if dp[i][a][b][c] != INF:
                    cnt1 = dif(a, value)
                    cnt2 = dif(b, value)
                    cnt3 = dif(c, value)
                    dp[i+1][value][b][c] = min(dp[i][a][b][c] + cnt1, dp[i+1][value][b][c])
                    dp[i+1][a][value][c] = min(dp[i][a][b][c] + cnt2, dp[i+1][a][value][c])
                    dp[i+1][a][b][value] = min(dp[i][a][b][c] + cnt3, dp[i+1][a][b][value])

ans = INF
for i in range(10):
    for j in range(10):
        for k in range(10):
            ans = min(ans, dp[N-1][i][j][k])
print(ans)