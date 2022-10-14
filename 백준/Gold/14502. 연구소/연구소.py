import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = []

from collections import deque
virus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append([i,j])
for a in range(N):
    for b in range(M):
        if graph[a][b] == 0:
            graph[a][b] = 1
            for c in range(N):
                for d in range(M):
                    if graph[c][d] == 0:
                        graph[c][d] = 1
                        for e in range(N):
                            for f in range(M):
                                if graph[e][f] == 0:
                                    graph[e][f] = 1
                                    queue = deque()
                                    true = [[-1]*(M) for i in range(N)]
                                    for node in virus:
                                        queue.append(node)
                                        true[node[0]][node[1]] = 0
                                    while queue:
                                        x, y = queue.popleft()
                                        for i in range(4):
                                            nx = x + dx[i]
                                            ny = y + dy[i]
                                            if 0<=nx<N and 0<=ny<M:
                                                if graph[nx][ny] == 0:
                                                    if true[nx][ny] == -1:
                                                        true[nx][ny] = true[x][y] + 1
                                                        queue.append([nx,ny])
                                    count = 0
                                    for i in range(N):
                                        for j in range(M):
                                            if graph[i][j] == 0 and true[i][j] == -1:
                                                count += 1
                                    ans.append(count)
                                    graph[e][f] = 0
                        graph[c][d] = 0
            graph[a][b] = 0
print(max(ans))