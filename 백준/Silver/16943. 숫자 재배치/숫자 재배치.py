import sys
input = sys.stdin.readline
A, B = map(str, input().split())
A = list(A)
import itertools
A = itertools.permutations(A)
Max = -1
for i in A:
    if i[0] == "0":
        continue
    A = "".join(i)
    if int(A) < int(B):
        Max = max(Max, int(A))
print(Max)
