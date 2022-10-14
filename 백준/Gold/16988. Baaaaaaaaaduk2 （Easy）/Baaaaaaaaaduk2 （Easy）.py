import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]

from collections import deque
queue = deque()
true = [[0]*M for i in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
List = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2 and true[i][j] == 0:
            List.append([[i,j]])
            true[i][j] = 1
            queue.append([i,j])
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<M:
                        if true[nx][ny] == 0 and graph[nx][ny] == 2:
                            List[-1].append([nx, ny])
                            queue.append([nx, ny])
                            true[nx][ny] = 1

ans = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            for a in range(N):
                for b in range(M):
                    if a == i and b == j:
                        continue
                    if graph[a][b] == 0:
                        graph[i][j] = 1
                        graph[a][b] = 1
                        Sum = 0
                        for k in List:
                            check = 0
                            for x, y in k:
                                for m in range(4):
                                    nx = x + dx[m]
                                    ny = y + dy[m]
                                    if 0<=nx<N and 0<=ny<M:
                                        if graph[nx][ny] == 0:
                                            check = 1
                                            break
                                if check == 1:
                                    break
                            if check == 0:
                                Sum += len(k)
                        ans = max(ans, Sum)
                        graph[i][j] = 0
                        graph[a][b] = 0
print(ans)