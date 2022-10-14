import sys
input = sys.stdin.readline
from collections import deque

def BFS(now, dest, true, dist, Max, From):
    queue = deque()
    true[now] = 1
    queue.append(now)
    while queue:
        current = queue.popleft()
        if current-1 >= 0 and true[current-1] == 0:
            true[current-1] = 1
            queue.append(current-1)
            dist[current-1] = dist[current] + 1
            From[current-1] = current
            if current-1 == dest:
                print(dist[current-1])
                return
        if current*2 < Max and true[current*2] == 0:
            true[current*2] = 1
            queue.append(current*2)
            dist[current*2] = dist[current] + 1
            From[current*2] = current
            if current*2 == dest:
                print(dist[current*2])
                return
        if current+1 < Max and true[current+1] == 0:
            true[current+1] = 1
            queue.append(current+1)
            dist[current+1] = dist[current] + 1
            From[current+1] = current
            if current+1 == dest:
                print(dist[current+1])
                return
    return
now, dest = map(int,input().split())
Max = 200000
true = [0]*(Max+1)
dist = [0]*(Max+1)
From = [0]*(Max+1)
if now == dest:
    print(0)
    print(now)
else:
    stack = deque()
    BFS(now, dest, true, dist, Max, From)
    stack.append(dest)
    while dest != now:
        dest = From[dest]
        stack.append(dest)
    for dest in range(len(stack)-1,-1,-1):
        print(stack[dest], end = " ")