import sys
input = sys.stdin.readline
N = int(input())
Mod = 1000000000
DP = [0]*1000001
DP[2] = 1
DP[3] = 2
for i in range(4,N+1):
    DP[i] = ((DP[i-1]+DP[i-2])*(i-1)) % Mod
print(DP[N])