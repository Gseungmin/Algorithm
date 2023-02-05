import sys
lines = sys.stdin.readlines()

List = []
for line in lines:
    A, B = map(int, line.split())
    List.append([A,B])

dp = [[[[[-1]*16 for d in range(16)] for c in range(2)] for b in range(2)] for a in range(len(List))] # 인덱스, 백, 흑, 남은 백, 남은 흑
dp[0][1][0][14][15] = List[0][0]
dp[0][0][1][15][14] = List[0][1]
dp[0][0][0][15][15] = 0

Max = 0
for i in range(len(List)-1):
    for j in range(2):
        for k in range(2):
            for m in range(16):
                for t in range(16):
                    if dp[i][j][k][m][t] != -1:
                        if m >= 1: #백을 선택할 수 있는 경우
                            dp[i+1][1][0][m-1][t] = max(dp[i+1][1][0][m-1][t], dp[i][j][k][m][t] + List[i+1][0])
                        if t >= 1: #흑을 선택할 수 있는 경우
                            dp[i+1][0][1][m][t-1] = max(dp[i+1][0][1][m][t-1], dp[i][j][k][m][t] + List[i+1][1])
                        #아무것도 선택 안하는 경우
                        dp[i+1][0][0][m][t] = max(dp[i+1][0][0][m][t], dp[i][j][k][m][t])
                        
for i in range(2):
    for j in range(2):
        Max = max(dp[len(List)-1][i][j][0][0], Max)
print(Max)