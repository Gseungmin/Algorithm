import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
graph = [[] for i in range(N+1)]
ind = [0]*(N+1)
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    ind[b] += 1

true = [0]*(N+1)
from collections import deque
for i in range(K):
    n, x = map(int,input().split())
    if n == 1:
        if ind[x] == 0:
            true[x] = true[x]+1
            for nx in graph[x]:
                if true[x] == 1:
                    ind[nx] -= 1
        else:
            print("Lier!")
            sys.exit()
    elif n == 2:
        if true[x] == 0:
            print("Lier!")
            sys.exit()
        true[x] = true[x]-1
        if true[x] == 0:
            for nx in graph[x]:
                ind[nx] += 1
print("King-God-Emperor")