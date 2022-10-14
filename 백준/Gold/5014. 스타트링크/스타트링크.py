import sys
input = sys.stdin.readline
F, S, G, U, D = map(int,input().split())
true = [-1]*(F+1)
from collections import deque
queue = deque()
queue.append(S)
true[S] = 0
while queue:
    x = queue.popleft()
    ux = x + U
    dx = x - D
    if ux <= F:
        if true[ux] == -1:
            queue.append(ux)
            true[ux] = true[x] + 1
    if  dx >= 1:
        if true[dx] == -1:
            queue.append(dx)
            true[dx] = true[x] + 1
if true[G] == -1:
    print("use the stairs")
else:
    print(true[G])