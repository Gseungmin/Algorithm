import sys
input = sys.stdin.readline
E, S, M = map(int,input().split())
Y = 0
e = 0
s = 0
m = 0
while 1:
    Y += 1
    e += 1
    s += 1
    m += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    if E == e and S == s and M == m:
        print(Y)
        break