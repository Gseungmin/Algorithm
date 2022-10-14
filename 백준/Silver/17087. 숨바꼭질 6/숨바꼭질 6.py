import sys
input = sys.stdin.readline
N, S = map(int, input().split())
A = list(map(int, input().split()))
for i in range(len(A)):
    A[i] = A[i] - S
    if A[i] < 0:
        A[i] = -A[i]
if len(A) == 1:
    print(A[0])
else:
    while len(A) != 1:
        a = A[0]
        b = A[1]
        while b != 0:
            a, b = b, a%b
        A[1] = a
        A.pop(0)
    print(A[0])