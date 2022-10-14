import sys
input = sys.stdin.readline
N = int(input())
Tree = [[] for i in range(N+1)]
for i in range(N-1):
    A, B = map(int,input().split())
    Tree[A].append(B)
    Tree[B].append(A)
    
true = [-1]*(N+1)
true[0] = 0
from collections import deque
queue = deque()
queue.append(1)
while queue:
    parent = queue.popleft()
    for child in Tree[parent]:
        if true[child] == -1:
            true[child] = parent
            queue.append(child)
for i in range(2,N+1):
    print(true[i])