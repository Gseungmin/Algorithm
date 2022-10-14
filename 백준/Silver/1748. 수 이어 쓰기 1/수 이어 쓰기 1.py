import sys
input = sys.stdin.readline
N = int(input())
Sum = 0
i = 1
j = 1
while 1:
    if N // (10*i) != 0:
        Sum += (10*i - i)*j
        i *= 10
        j += 1
    else:
        Sum += (N - i + 1) * j
        break
print(Sum)
