import sys
input = sys.stdin.readline
A_size, B_size = map(int,input().split())
from collections import deque
A = deque(map(int,input().split()))
B = deque(map(int,input().split()))
while A and B:
    if A[0] < B[0]:
        print(A.popleft(), end = " ")
    else:
        print(B.popleft(), end = " ")
while A:
    print(A.popleft(), end = " ")
while B:
    print(B.popleft(), end = " ")
