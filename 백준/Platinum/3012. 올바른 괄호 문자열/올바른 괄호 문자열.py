import sys
input = sys.stdin.readline
N = int(input())
s = input()
dp = [[-1]*200 for i in range(200)]
op = "{[("
cl = "}])"

def DP(start, end):
    if start > end:
        return 1
    if dp[start][end] != -1:
        return dp[start][end]
    k = 0
    for i in range(start+1, end+1):
        for j in range(3):
            if s[start] == op[j] or s[start] == "?":
                if s[i] == cl[j] or s[i] == "?":
                    k += DP(start+1, i-1)*DP(i+1, end)
    dp[start][end] = k
    return k

print(str(DP(0,N-1))[-5:])