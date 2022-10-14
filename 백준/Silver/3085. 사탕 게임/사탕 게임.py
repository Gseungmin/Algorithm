import sys
input = sys.stdin.readline
N = int(input())
Map = [list(input()[:-1]) for i in range(N)]

dx = [1,0]
dy = [0,1]

def Sum(x, y, N, Map):
    ch = Map[x][y]
    col = 1
    row = 1
    ux = x+1
    dx = x-1
    uy = y+1
    dy = y-1
    while ux < N:
        if Map[ux][y] == ch:
            col += 1
            ux +=1
        else:
            break
    while 0 <= dx:
        if Map[dx][y] == ch:
            col += 1
            dx -=1
        else:
            break
    while uy < N:
        if Map[x][uy] == ch:
            row += 1
            uy +=1
        else:
            break
    while 0 <= dy:
        if Map[x][dy] == ch:
            row += 1
            dy -=1
        else:
            break
    return max(col, row)

Max = 1
for i in range(N):
    for j in range(N):
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<N and 0<=ny<N:
                Map[nx][ny], Map[i][j] = Map[i][j], Map[nx][ny]
                Sum1 = Sum(i,j,N,Map)
                Sum2 = Sum(nx,ny,N,Map)
                Max = max(Max, Sum1, Sum2)
                Map[nx][ny], Map[i][j] = Map[i][j], Map[nx][ny]
print(Max)