import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    C = A*B
    while B != 0: #until B is 0
        A, B = B, A%B
    print(C//A)