import sys
input = sys.stdin.readline
N = int(input()) #size of sequence
A = list(map(int,input().split())) #sequence
memo = [1]*N
for i in range(1,N):
    for j in range(i):
        if A[i] < A[j]:
            memo[i] = max(memo[i], memo[j]+1)
print(max(memo))