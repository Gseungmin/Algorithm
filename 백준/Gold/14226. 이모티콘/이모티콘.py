import sys
input = sys.stdin.readline
S = int(input())

graph = [[-1]*(S+1) for i in range(S+1)]

from collections import deque
def BFS(graph, S, x, y):
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 0
    while queue:
        s, c = queue.popleft()
        if graph[s][s] == -1:
            graph[s][s] = graph[s][c] + 1
            queue.append([s,s])
            if S == s:
                print(graph[s][s])
                sys.exit()
        if s-1 > 0:
            if graph[s-1][c] == -1:
                graph[s-1][c] = graph[s][c] + 1
                queue.append([s-1,c])
                if S == s-1:
                    print(graph[s-1][c])
                    sys.exit()
        if s+c <= S:
            if graph[s+c][c] == -1:
                graph[s+c][c] = graph[s][c] + 1
                queue.append([s+c,c])
                if S == s+c:
                    print(graph[s+c][c])
                    sys.exit()
    return

BFS(graph, S, 1, 0)