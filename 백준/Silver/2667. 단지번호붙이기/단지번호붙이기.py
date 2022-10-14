N = int(input())
graph = []
true = []
for i in range(N):
    graph.append(list(map(int,list(input()))))
    true.append([0]*N)

dx = [-1,1,0,0] #x좌표의 이동반경
dy = [0,0,1,-1] #y좌표의 이동반경

ans = []

def BFS(graph, x, y, true, dx, dy, ans):
    queue = []
    queue.append([x,y])
    true[x][y] = 1
    Sum = 0
    while queue:
        a, b = queue.pop(0)
        Sum += 1
        for i in range(4):
            c = a + dx[i]
            d = b + dy[i]
            if ((0<=c) and (c<N)) and ((0<=d) and (d<N)):
                if (true[c][d] == 0) and (graph[c][d] == 1):
                    true[c][d] = 1
                    queue.append([c,d])
    ans.append(Sum)
    return  

Sum = 0
for i in range(N):
    for j in range(N):
        if (graph[i][j] == 1) and (true[i][j] == 0):
            Sum += 1
            BFS(graph, i, j, true, dx, dy, ans)
          
print(Sum)
ans.sort()
for i in ans:
    print(i)