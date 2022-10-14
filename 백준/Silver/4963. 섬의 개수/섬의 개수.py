def BFS(graph, x, y, true, dx, dy, W, H):
    queue = []
    queue.append([x,y])
    true[x][y] = 1
    while queue:
        a, b = queue.pop(0)
        for i in range(8):
            c = a + dx[i]
            d = b + dy[i]
            if ((0<=c) and (c<W)) and ((0<=d) and (d<H)):
                if (true[c][d] == 0) and (graph[c][d] == 1):
                    true[c][d] = 1
                    queue.append([c,d])
    return

while 1:
    H, W = map(int,input().split())
    if H == 0 and W == 0:
        break
    graph = []
    true = []
    for i in range(W):
        graph.append(list(map(int,input().split())))
        true.append([0]*H)

    dx = [-1,1,0,0,-1,-1,1,1] #x좌표의 이동반경
    dy = [0,0,1,-1,-1,1,-1,1] #y좌표의 이동반경

    ans = []

    Sum = 0
    for i in range(W):
        for j in range(H):
            if (graph[i][j] == 1) and (true[i][j] == 0):
                Sum += 1
                BFS(graph, i, j, true, dx, dy, W, H)
          
    print(Sum)