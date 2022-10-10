import sys
input = sys.stdin.readline
import math
N, R, G, B = map(int,input().split())
dp = [[[[0]*(B+1) for i in range(G+1)] for j in range(R+1)] for k in range(N+1)]
from collections import deque
queue = deque()
queue.append([0,R,G,B])
dp[0][R][G][B] = 1
for k in range(N):
    for r in range(R+1):
        for g in range(G+1):
            for b in range(B+1):
                if dp[k][r][g][b] != 0:
                    f = math.factorial(k+1)
                    if r >= k+1:    
                        dp[k+1][r-k-1][g][b] += dp[k][r][g][b]
                        queue.append([k+1,r-k-1,g,b])
                    if g >= k+1:        
                        dp[k+1][r][g-k-1][b] += dp[k][r][g][b]
                        queue.append([k+1,r,g-k-1,b])
                    if b >= k+1:
                        dp[k+1][r][g][b-k-1] += dp[k][r][g][b]
                        queue.append([k+1,r,g,b-k-1])
                    if (k+1)%2 == 0:
                        m = (k+1)//2
                        if r >= m and g >= m:
                            dp[k+1][r-m][g-m][b] += dp[k][r][g][b]*(f//(math.factorial(m)**2))
                            queue.append([k+1,r-m,g-m,b])
                        if r >= m and b >= m:
                            dp[k+1][r-m][g][b-m] += dp[k][r][g][b]*(f//(math.factorial(m)**2))
                            queue.append([k+1,r-m,g,b-m])
                        if b >= m and g >= m:
                            dp[k+1][r][g-m][b-m] += dp[k][r][g][b]*(f//(math.factorial(m)**2))
                            queue.append([k+1,r,g-m,b-m])
                    if (k+1)%3 == 0:
                        m = (k+1)//3
                        if r >= m and g >= m and b >= m:
                            dp[k+1][r-m][g-m][b-m] += dp[k][r][g][b]*(f//(math.factorial(m)**3))
                            queue.append([k+1,r-m,g-m,b-m])
ans = 0
for i in range(R+1):
    for j in range(G+1):
        for k in range(B+1):
            ans += dp[N][i][j][k]
print(ans)