import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    K, M, P = map(int,input().split())
    graph = [[] for i in range(M+1)]
    check = [[] for i in range(M+1)]
    ind = [0]*(M+1)
    for i in range(P):
        a, b = map(int,input().split())
        graph[a].append(b)
        ind[b] += 1
    true = [0]*(M+1)
    queue = deque()
    for i in range(1,M+1):
        if ind[i] == 0:
            true[i] = 1
            queue.append(i)
    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if true[nx] == 0:
                check[nx].append(true[x])
                ind[nx] -= 1
                if ind[nx] == 0:
                    Max = max(check[nx])
                    cnt = 0
                    for i in check[nx]:
                        if i == Max:
                            cnt += 1
                            if cnt == 2:
                                break
                    if cnt == 2:
                        true[nx] = Max+1
                    else:
                        true[nx] = Max
                    queue.append(nx)
    print(K, max(true))