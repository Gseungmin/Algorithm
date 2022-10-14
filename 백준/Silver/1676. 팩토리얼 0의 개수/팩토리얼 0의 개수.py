import sys
input = sys.stdin.readline
N = int(input()) #N!
if N == 0:
    print(0)
else:
    i = 5
    Sum = 0
    while i <= N:
        Sum += N//i
        i *= 5
    print(Sum)