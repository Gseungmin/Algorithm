import sys #for using sys
input = sys.stdin.readline
N = int(input()) #size of seq
seq = list(map(int, input().split()))
memo = [1]*N
for i in range(1,N):
    M = memo[i]
    for j in range(i):
        if seq[j] < seq[i]:
            memo[i] = max(memo[i], M+memo[j])
print(max(memo))