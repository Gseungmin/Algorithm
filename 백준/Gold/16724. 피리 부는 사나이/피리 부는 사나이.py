import sys
input = sys.stdin.readline

#1:28
#4가지 방향으로 이동
#사이클 개수 구하고 한 사이클 구할때마다 모든 연결 제거

N, M = map(int,input().split())

graph = [list(input().rstrip()) for i in range(N)]

direct = dict()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
direct["D"] = 1
direct["U"] = 0
direct["L"] = 2
direct["R"] = 3

true = [[False]*M for i in range(N)]

def DFS(x,y,Set):
    
    true[x][y] = True
    Set.add((x,y))
    k = direct[graph[x][y]]
    
    nx, ny = x+dx[k], y+dy[k]
    if 0<=nx<N and 0<=ny<M:
        if true[nx][ny] == True:
            if (nx,ny) in Set:
                check[0] = True
                return
        else:
            DFS(nx,ny,Set)
    return

cnt = 0
for i in range(N):
    for j in range(M):
        if true[i][j] == False:
            check = [False]
            DFS(i,j,set())
            if check[0] == True:
                cnt += 1
print(cnt)