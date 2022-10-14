def BFS(graph, x, y, true, dx, dy, N, M, ans):
    queue = []
    queue.append([x,y])
    true[x][y] = 1
    while queue:
        a, b = queue.pop(0)
        for i in range(4):
            c = a + dx[i]
            d = b + dy[i]
            if ((0<=c) and (c<N)) and ((0<=d) and (d<M)):
                if (true[c][d] == 0) and (graph[c][d] == 1):
                    true[c][d] = 1
                    queue.append([c,d])
                    ans[c][d] = ans[a][b] + 1
    return
N, M = map(int,input().split())
graph = []
true = []
ans = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
for i in range(N):
    graph.append(list(map(int,list(input()))))
    true.append([0]*M)
    ans.append([1]*M)
BFS(graph, 0, 0, true, dx, dy, N, M, ans)
print(ans[N-1][M-1])