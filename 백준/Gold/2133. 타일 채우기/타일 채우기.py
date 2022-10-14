import sys
input = sys.stdin.readline
N = int(input())
memo = [0] * (31)
memo[0] = 1
memo[2] = 3
memo[4] = 11
for i in range(6,31,2):
    memo[i] = 3*memo[i-2]
    j = i - 2
    while j != 0:
        j -= 2
        memo[i] += 2*memo[j]
if N % 2 != 0:
    print(0)
else:
    print(memo[N])