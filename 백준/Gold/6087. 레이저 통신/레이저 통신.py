M, N = map(int,input().split())
graph = [list(input()) for i in range(N)]
from collections import deque
def BFS(graph, N, M, x, y, true):
    queue = deque()
    queue.append([x,y])
    true[x][y] = 0
    while queue:
        a, b = queue.popleft()
        nx1 = a + 1
        nx2 = a - 1
        ny1 = b + 1
        ny2 = b - 1
        while 0<=nx1<N:
            if true[nx1][b] == -1 or true[nx1][b] > true[a][b]:
                if graph[nx1][b] == '*':
                    break
                else:
                    true[nx1][b] = true[a][b] + 1
                    queue.append([nx1,b])
                    if graph[nx1][b] == 'C':
                        print(true[a][b])
                        exit()
                        return
                    nx1 += 1
            else:
                break
        while 0<=nx2<N:
            if true[nx2][b] == -1 or true[nx2][b] > true[a][b]:
                if graph[nx2][b] == '*':
                    break
                else:
                    true[nx2][b] = true[a][b] + 1
                    queue.append([nx2,b])
                    if graph[nx2][b] == 'C':
                        print(true[a][b])
                        exit()
                        return
                    nx2 -= 1
            else:
                break
        while 0<=ny1<M:
            if true[a][ny1] == -1 or true[a][ny1] > true[a][b]:
                if graph[a][ny1] == '*':
                    break
                else:
                    true[a][ny1] = true[a][b] + 1
                    queue.append([a,ny1])
                    if graph[a][ny1] == 'C':
                        print(true[a][b])
                        exit()
                        return
                    ny1 += 1
            else:
                break
        while 0<=ny2<M:
            if true[a][ny2] == -1 or true[a][ny2] > true[a][b]:
                if graph[a][ny2] == '*':
                    break
                else:
                    true[a][ny2] = true[a][b] + 1
                    queue.append([a,ny2])
                    if graph[a][ny2] == 'C':
                        print(true[a][b])
                        exit()
                        return
                    ny2 -= 1
            else:
                break
    return

true = [[-1]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'C':
            BFS(graph, N, M, i, j, true) 