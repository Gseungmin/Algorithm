import sys
input = sys.stdin.readline
N = int(input()) #size of sequence
A = list(map(int,input().split())) #sequence
Sum = A
for i in range(N):
    origin = Sum[i]
    for j in range(i):
        if A[i] > A[j]:
            Sum[i] = max(Sum[i], origin + A[j])
print(max(Sum))