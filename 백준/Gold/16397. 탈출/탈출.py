import sys
input = sys.stdin.readline
N, T, G = map(int,input().split())
dist = [-1]*(100000)

from collections import deque
queue = deque()
queue.append(N)
dist[N] = 0
while queue:
    x = queue.popleft()
    if dist[x] == T:
        continue
    nx1 = x+1
    nx2 = x*2
    if nx1 <= 99999:
        if dist[nx1] == -1:
            dist[nx1] = dist[x] + 1
            queue.append(nx1)
    if nx2 <= 99999:
        if nx2 == 0:
            if dist[nx2] == -1:
                dist[nx2] = dist[x] + 1
                queue.append(nx2)
        else:
            nx2 = nx2-10**(len(str(nx2))-1)
            if dist[nx2] == -1:
                dist[nx2] = dist[x] + 1
                queue.append(nx2)
if dist[G] == -1:
    print("ANG")
else:
    print(dist[G])