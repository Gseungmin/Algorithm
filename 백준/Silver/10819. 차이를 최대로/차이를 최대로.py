import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))

import itertools
nPr = itertools.permutations(A)

def Per(List, N):
    Sum = 0
    for i in range(1,N):
        Sum += abs(List[i]-List[i-1])
    return Sum

Max = -1    
for List in nPr:
    Max = max(Max, Per(List, N))
print(Max)