import sys
input = sys.stdin.readline
N = int(input())
i = 2
while N != 1:
    while N % i == 0: #if i is a divisor of N
        N = N // i
        print(i)
    i += 1