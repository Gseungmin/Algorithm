import sys
input = sys.stdin.readline
N = int(input())
if N == 0:
    print(1)
else:
    j = 1
    for k in range(1, N+1):
        j *= k
    print(j)