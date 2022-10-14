N, M = map(int,input().split())
graph = []
true = [0]*26
ans = [0]
for i in range(N):
    graph.append(list(input()))
for i in range(N):
    for j in range(M):
        graph[i][j] = ord(graph[i][j])-65
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def move(graph, x, y, dx, dy, N, M, true, total, ans):
    true[graph[x][y]] = 1
    check = 0
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0<=a<N and 0<=b<M:
            if true[graph[a][b]] == 0:
                check = 1
                true[graph[a][b]] = 1
                move(graph, a, b, dx, dy, N, M, true, total+1, ans)
                true[graph[a][b]] = 0
    if check == 0:
        if ans[0] == 0 or ans[0] < total:
            ans[0] = total
    return

move(graph, 0, 0, dx, dy, N, M, true, 1, ans)
print(ans[0])