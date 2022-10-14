import sys
input = sys.stdin.readline
K, E, W, S, N = map(int,input().split())
true = [[-1]*29 for i in range(29)]
true[14][14] = 1
Set = set()
Str = []
ds = ["E","W","S","N"]
direct = [E,W,S,N]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = [0]
def DFS(x,y):
    if len(Str) == K:
        ans[0] += true[x][y]
        return
    for i in range(4):
        if direct[i] != 0:
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<29 and 0<=ny<29:
                if true[nx][ny] == -1:
                    true[nx][ny] = true[x][y]*(direct[i]/100)
                    Str.append(ds[i])
                    DFS(nx,ny)
                    Str.pop()
                    true[nx][ny] = -1
    return
DFS(14,14)
print(ans[0])