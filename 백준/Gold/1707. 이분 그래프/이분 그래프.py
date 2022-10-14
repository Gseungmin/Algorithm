from collections import deque
def BFS(start, graph, true):
    queue = deque()
    queue.append(start)
    true[start] = 1
    while queue:
        now = queue.popleft()
        for Next in graph[now]:
            if true[Next] == 0:
                queue.append(Next)
                true[Next] = 3 - true[now]
            if true[now] == true[Next]:
                true[0] = -1
                return
    return

import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    V, E = map(int,input().split())
    graph = [[] for i in range(V+1)]
    true = [0]*(V+1)
    for i in range(E):
        A, B = map(int,input().split())
        graph[A].append(B)
        graph[B].append(A)
    for i in range(1,V+1):
        if true[i] == 0:
            BFS(i, graph, true)
    if true[0] == -1:
        print('NO')
    else:
        print('YES')