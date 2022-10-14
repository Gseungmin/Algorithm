import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]
from collections import deque
def BFS(graph, x, y, dx, dy, true, size):
    queue = deque()
    queue.append([x,y])
    true[x][y] = 0
    eat = []
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if true[nx][ny] == -1 and graph[nx][ny] <= size:
                    queue.append([nx,ny])
                    true[nx][ny] = true[a][b] + 1
                    if 0 < graph[nx][ny] < size:
                        if eat:
                            if eat[-1][0] < true[nx][ny]:
                                eat.sort()
                                graph[eat[0][1]][eat[0][2]] = 0
                                return eat
                            else:
                                eat.append([true[nx][ny], nx, ny])
                        else:
                            eat.append([true[nx][ny], nx, ny])
    if eat:
        eat.sort()
        graph[eat[0][1]][eat[0][2]] = 0
        return eat
    return -1
for x in range(N):
    for y in range(N):
        if graph[x][y] == 9:
            break
    if graph[x][y] == 9:
        break
graph[x][y] = 0
total = 0
check = 0
cnt = 0
size = 2
while 1:
    true = [[-1]*N for i in range(N)]
    ans = BFS(graph, x, y, dx, dy, true, size)
    if check == 0 and ans == -1:
        print(0)
        break
    elif check != 0 and ans == -1:
        print(total)
        break
    check = 1
    x = ans[0][1]
    y = ans[0][2]
    total += ans[0][0]
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0