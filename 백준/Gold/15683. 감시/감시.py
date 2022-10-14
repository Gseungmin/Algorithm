import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
Max = [N*M]


def RC(index, graph, Max, N, M):
    if index == N*M:
        total = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    total += 1
        Max[0] = min(Max[0], total)
        return
    x, y = index//M, index%M
    if graph[x][y] == 1:
        List = []
        ly(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
        List = []
        ry(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
        List = []
        ux(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
        List = []
        dx(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
    elif graph[x][y] == 2:
        List = []
        ly(x, y, N, M, graph, List)
        ry(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
        List = []
        ux(x, y, N, M, graph, List)
        dx(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
    elif graph[x][y] == 3:
        List = []
        ly(x, y, N, M, graph, List)
        ux(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
        List = []
        ry(x, y, N, M, graph, List)
        dx(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
        List = []
        ly(x, y, N, M, graph, List)
        dx(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
        List = []
        ry(x, y, N, M, graph, List)
        ux(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
    elif graph[x][y] == 4:
        List = []
        ly(x, y, N, M, graph, List)
        ry(x, y, N, M, graph, List)
        ux(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
        List = []
        ly(x, y, N, M, graph, List)
        ry(x, y, N, M, graph, List)
        dx(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
        List = []
        ly(x, y, N, M, graph, List)
        ux(x, y, N, M, graph, List)
        dx(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
        List = []
        ry(x, y, N, M, graph, List)
        ux(x, y, N, M, graph, List)
        dx(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
    elif graph[x][y] == 5:
        List = []
        ry(x, y, N, M, graph, List)
        ux(x, y, N, M, graph, List)
        dx(x, y, N, M, graph, List)
        ly(x, y, N, M, graph, List)
        RC(index+1, graph, Max, N, M)
        for i in List:
            graph[i[0]][i[1]] = 0
    else:
        RC(index+1, graph, Max, N, M)
    return

def ly(x, y, N, M, graph, List):
    ny = y-1
    while ny>=0:
        if graph[x][ny] == 6:
            break
        if graph[x][ny] == 0:
            graph[x][ny] = "#"
            List.append([x,ny])
        ny -= 1
    return
def ry(x, y, N, M, graph, List):
    ny = y+1
    while ny<M:
        if graph[x][ny] == 6:
            break
        if graph[x][ny] == 0:
            graph[x][ny] = "#"
            List.append([x,ny])
        ny += 1
    return
def ux(x, y, N, M, graph, List):
    nx = x-1
    while nx>=0:
        if graph[nx][y] == 6:
            break
        if graph[nx][y] == 0:
            graph[nx][y] = "#"
            List.append([nx,y])
        nx -= 1
    return
def dx(x, y, N, M, graph, List):
    nx = x+1
    while nx<N:
        if graph[nx][y] == 6:
            break
        if graph[nx][y] == 0:
            graph[nx][y] = "#"
            List.append([nx,y])
        nx += 1
    return

RC(0, graph, Max, N, M)
print(Max[0])