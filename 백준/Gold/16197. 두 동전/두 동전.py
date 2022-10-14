N, M = map(int,input().split())
graph = [list(input()) for i in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = [11]
def RC(k, x1, y1, x2, y2, ans):
    if k >= 10:
        return
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        if 0<=nx1<N and 0<=ny1<M and 0<=nx2<N and 0<=ny2<M:
            if graph[nx1][ny1] != "#" and graph[nx2][ny2] != "#":
                RC(k+1, nx1, ny1, nx2, ny2, ans)
            elif graph[nx1][ny1] != "#" and graph[nx2][ny2] == "#":
                RC(k+1, nx1, ny1, x2, y2, ans)
            elif graph[nx1][ny1] == "#" and graph[nx2][ny2] != "#":
                RC(k+1, x1, y1, nx2, ny2, ans)
        elif (0<=nx1<N and 0<=ny1<M) and (nx2>=N or nx2<0 or ny2>=M or ny2<0):
            ans[0] = min(ans[0], k+1)
            return
        elif (0<=nx2<N and 0<=ny2<M) and (nx1>=N or nx1<0 or ny1>=M or ny1<0):
            ans[0] = min(ans[0], k+1)
            return
    return
List = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == "o":
            List.append([i,j])
x1, y1, x2, y2 = List[0][0], List[0][1], List[1][0], List[1][1]
RC(0, x1, y1, x2, y2, ans)
if ans[0] != 11:
    print(ans[0])
else:
    print(-1)