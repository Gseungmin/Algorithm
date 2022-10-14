R, C, T = map(int,input().split())
graph = [list(input()) for i in range(R)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def RC(x,y,t,cnt):
    if t == T:
        ans[0] = max(ans[0], cnt)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C:
            if graph[nx][ny] == "#":
                continue
            if graph[nx][ny] == "S":
                if (nx,ny) in true: 
                    RC(nx,ny,t+1,cnt)
                else:
                    true.add((nx,ny))
                    RC(nx,ny,t+1,cnt+1)
                    true.discard((nx,ny))
            else:
                RC(nx,ny,t+1,cnt)
    return

for i in range(R):
    for j in range(C):
        if graph[i][j] == "G":
            true = set()
            ans = [0]
            RC(i,j,0,0)
            print(ans[0])
            exit()