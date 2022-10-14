N, M = map(int,input().split())
graph = [list(map(int,list(input()))) for i in range(N)]
true = [[0]*M for i in range(N)]
List = [0,0]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
from collections import deque
def BFS(graph, a, b, dx, dy, true, num):
    queue = deque()
    queue.append([a,b])
    true[a][b] = 1
    graph[a][b] = num
    total = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if true[nx][ny] == 0 and graph[nx][ny] == 0: #방문한 적이 없으면
                    total += 1
                    true[nx][ny] = true[x][y] + 1
                    graph[nx][ny] = num
                    queue.append([nx,ny])
    return total
group = 2
for i in range(N):
    for j in range(M):
        if true[i][j] == 0 and graph[i][j] != 1:
            total = BFS(graph, i, j, dx, dy, true, group)
            List.append(total)
            group += 1
ans = [[0]*M for i in range(N)]
for x in range(N):
    for y in range(M):
        All = set()
        if graph[x][y] == 1:
            ans[x][y] += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if graph[nx][ny] == 1:
                        continue
                    All.add(graph[nx][ny])
        for i in All:
            ans[x][y] += List[i]
for i in range(N):
    for j in range(M):
        ans[i][j] = ans[i][j] % 10
        if j == M-1:
            print(ans[i][j])
        else:
            print(ans[i][j], end = "")