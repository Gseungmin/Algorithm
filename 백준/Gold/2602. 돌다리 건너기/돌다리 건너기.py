import sys
input = sys.stdin.readline
S = list(input().rstrip())
left = list(input().rstrip())
right = list(input().rstrip())

#dp[i][j][k] = i번째에 j번째를 물고 k

N = len(left)

dp = [[[0]*2 for i in range(N)] for j in range(len(S))]

#초기 설정
for i in range(N):
    if left[i] == S[0]:
        dp[0][i][0] = 1
    if right[i] == S[0]:
        dp[0][i][1] = 1

for i in range(len(S)-1):
    for j in range(N):
        for k in range(2):
            if dp[i][j][k] != 0: #0이 아닌 경우
                for m in range(j+1,N):
                    if k == 0:
                        if S[i+1] == right[m]:
                            dp[i+1][m][1] += dp[i][j][k]
                    elif k == 1:
                        if S[i+1] == left[m]:
                            dp[i+1][m][0] += dp[i][j][k]
Sum = 0
for i in range(N):
    for j in range(2):
        if dp[-1][i][j] != 0:
            Sum += dp[-1][i][j]

print(Sum)