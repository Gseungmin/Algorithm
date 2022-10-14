import sys
input = sys.stdin.readline
A, B = map(int,input().split())

from collections import deque
queue = deque()
queue.append([A,0])
check = set()
check.add(A)
while queue:
    x, y = queue.popleft()
    if x == B:
        print(y+1)
        sys.exit()
    if x*2 <= 10**9:
        if x*2 not in check:
            queue.append([x*2,y+1])
    if 10*x+1 <= 10**9:
        if 10*x+1 not in check:
            queue.append([10*x+1,y+1])
print(-1)