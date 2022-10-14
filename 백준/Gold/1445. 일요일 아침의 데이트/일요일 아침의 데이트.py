import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(input().strip()) for i in range(N)]
dist = dict()
INF = int(1e9)
import heapq
heap = []
for i in range(N):
    for j in range(M):
        dist[(i,j)] = [INF, INF]
        if graph[i][j] == "S":
            heapq.heappush(heap,[0,0,i,j])
            dist[(i,j)] = [0, 0]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
true = [[False]*M for i in range(N)]
while heap:
    t1, t2, x, y = heapq.heappop(heap)
    if true[x][y] == True:
        continue
    true[x][y] = True
    if graph[x][y] == "F":
        print(dist[(x,y)][0],dist[(x,y)][1])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if true[nx][ny] == False:
                check = False
                for j in range(4):
                    nnx = nx+dx[j]
                    nny = ny+dy[j]
                    if 0<=nnx<N and 0<=nny<M:
                        if graph[nnx][nny] == "g":
                            check = True
                            break
                if graph[nx][ny] == "g":
                    if dist[(nx,ny)][0] > dist[(x,y)][0]+1:
                        dist[(nx,ny)][0] = dist[(x,y)][0]+1
                        dist[(nx,ny)][1] = dist[(x,y)][1]
                        heapq.heappush(heap,[dist[(nx,ny)][0],dist[(nx,ny)][1],nx,ny])
                    elif dist[(nx,ny)][0] == dist[(x,y)][0]+1:
                        if dist[(nx,ny)][1] > dist[(x,y)][1]:
                            dist[(nx,ny)][1] = dist[(x,y)][1]
                        heapq.heappush(heap,[dist[(nx,ny)][0],dist[(nx,ny)][1],nx,ny])
                elif graph[nx][ny] == ".":
                    if dist[(nx,ny)][0] > dist[(x,y)][0]:
                        dist[(nx,ny)][0] = dist[(x,y)][0]
                        if check == True:
                            dist[(nx,ny)][1] = dist[(x,y)][1]+1
                        else:
                            dist[(nx,ny)][1] = dist[(x,y)][1]
                        heapq.heappush(heap,[dist[(nx,ny)][0],dist[(nx,ny)][1],nx,ny])
                    elif dist[(nx,ny)][0] == dist[(x,y)][0]:
                        if check == True:
                            if dist[(nx,ny)][1] > dist[(x,y)][1]+1:
                                dist[(nx,ny)][1] = dist[(x,y)][1]+1
                        else:
                            if dist[(nx,ny)][1] > dist[(x,y)][1]:
                                dist[(nx,ny)][1] = dist[(x,y)][1]
                        heapq.heappush(heap,[dist[(nx,ny)][0],dist[(nx,ny)][1],nx,ny])
                elif graph[nx][ny] == "F":
                    if dist[(nx,ny)][0] > dist[(x,y)][0]:
                        dist[(nx,ny)][0] = dist[(x,y)][0]
                        dist[(nx,ny)][1] = dist[(x,y)][1]
                        heapq.heappush(heap,[dist[(nx,ny)][0],dist[(nx,ny)][1],nx,ny])
                    elif dist[(nx,ny)][0] == dist[(x,y)][0]+1:
                        if dist[(nx,ny)][1] > dist[(x,y)][1]:
                            dist[(nx,ny)][1] = dist[(x,y)][1]
                        heapq.heappush(heap,[dist[(nx,ny)][0],dist[(nx,ny)][1],nx,ny])