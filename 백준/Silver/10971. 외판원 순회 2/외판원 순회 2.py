import sys
input = sys.stdin.readline
N = int(input())
W = [list(map(int,input().split())) for i in range(N)]

A = []
for i in range(1,N):
    A.append(i)

import itertools
nPr = list(itertools.permutations(A))

check = 0
Max = -1
for route in nPr:
    k = 0
    plus = W[0][route[k]]
    if plus == 0:
        continue
    Sum = plus
    while k < N-2:
        plus = W[route[k]][route[k+1]]
        if plus == 0:
            check = 1
            break
        Sum += plus
        k += 1
    if check == 1:
        check = 0
        continue
    plus = W[route[-1]][0]
    if plus == 0:
        continue
    Sum += plus
    if Max == -1:
        Max = Sum
    else:
        Max = min(Max, Sum)
print(Max)