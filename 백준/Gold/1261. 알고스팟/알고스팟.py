from collections import deque

def BFS(graph, x, y, dx, dy, f_x, f_y, true, dist):
    queue_1 = deque()
    queue_2 = deque()
    true[x][y] = 1
    queue_1.append([x,y])
    while queue_1:
        while queue_1:
            a,b = queue_1.popleft()
            for i in range(4):
                c = a + dx[i]
                d = b + dy[i]
                if (0<=c<N) and (0<=d<M):
                    if true[c][d] == 0:
                        if graph[c][d] == 0:
                            true[c][d] = 1
                            dist[c][d] = dist[a][b]
                            queue_1.append([c,d])
                            if c == f_x and d == f_y:
                                print(dist[c][d])
                                return
                        if graph[c][d] == 1:
                            true[c][d] = 1
                            dist[c][d] = dist[a][b] + 1
                            queue_2.append([c,d])
        queue_2, queue_1 = queue_1, queue_2
    return
M, N = map(int,input().split())
graph = []
true = []
dist = []
for i in range(N):
    graph.append(list(map(int,list(input()))))
    true.append([0]*M)
    dist.append([0]*M)
dx = [-1,1,0,0]
dy = [0,0,1,-1]
if N == 1 and M == 1:
    print(0)
else:
    BFS(graph, 0, 0, dx, dy, N-1, M-1, true, dist)