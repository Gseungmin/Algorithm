import sys
input = sys.stdin.readline
A, B = map(int, input().split())
C = A*B
while B != 0: #until B is 0
    A, B = B, A%B
print(A)
print(C//A)
