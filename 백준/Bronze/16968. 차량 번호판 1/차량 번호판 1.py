import sys
input = sys.stdin.readline
N = input()
Sum = 1
c = 0
d = 0
for i in N:
    if i == 'c':
        if c == 1:
            Sum *= 25
        else:
            Sum *= 26
        c = 1
        d = 0
    if i == 'd':
        if d == 1:
            Sum *= 9
        else:
            Sum *= 10
        d = 1
        c = 0
print(Sum)