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
Max = max(memo)
print(Max)
ans = []
M = N-1
while M > -1:
    if Max == memo[M]:
        ans.append(seq[M])
        Max -= 1
    M -= 1
for i in range(len(ans)-1,-1,-1):
    print(ans[i], end = " ")