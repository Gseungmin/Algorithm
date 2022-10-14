import sys
input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N+1)]
parent = dict()
Level = [-1]*(N+1)
Level[1] = 0
for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
queue = deque()
queue.append(1)
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if Level[nx] == -1:
            parent[nx] = x
            Level[nx] = Level[x]+1
            queue.append(nx)

M = int(input())
for i in range(M):
    a, b = map(int,input().split())
    if Level[a] > Level[b]:
        a, b = b, a
    while Level[a] != Level[b]:
        b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)