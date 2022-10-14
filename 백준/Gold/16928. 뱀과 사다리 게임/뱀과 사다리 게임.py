import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [0]*101
true = [0]*101
for i in range(N+M):
    a, b = map(int,input().split())
    graph[a] = b

from collections import deque
queue = deque()
queue.append(1)
while queue:
    x = queue.popleft()
    for i in range(1,7):
        nx = x + i
        if nx <= 100:
            if true[nx] == 0:
                if graph[nx] == 0:
                    true[nx] = true[x] + 1
                    queue.append(nx)
                else:
                    if true[graph[nx]] == 0:
                        true[nx] = true[x] + 1
                        queue.append(graph[nx])
                        true[graph[nx]] = true[x] + 1
        if true[100] != 0:
            print(true[100])
            sys.exit()