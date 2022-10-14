import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
A.sort()
for i in range(1,N):
    A[i] = A[i] + A[i-1]
print(sum(A))