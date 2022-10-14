import sys
input = sys.stdin.readline
from collections import deque
N, L, R = map(int,input().split())
Map = [list(map(int,input().split())) for i in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
day = 0
while 1:
    check = 0
    graph = dict()
    for x in range(N):
        for y in range(N):
            graph[(x,y)] = []
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<N and 0<=ny<N:
                    dif = abs(Map[nx][ny]-Map[x][y])
                    if L<=dif<=R:
                        check = 1
                        graph[(x,y)].append([nx,ny])
    if check == 0:
        print(day)
        sys.exit()
    true = [[False]*N for i in range(N)]
    for x in range(N):
        for y in range(N):
            if true[x][y] == False:
                List = []
                Sum, cnt = 0, 0
                true[x][y] = True
                queue = deque()
                queue.append([x,y])
                while queue:
                    i, j = queue.popleft()
                    List.append([i,j])
                    Sum += Map[i][j]
                    cnt += 1
                    for nx, ny in graph[(i,j)]:
                        if true[nx][ny] == False:
                            queue.append([nx,ny])
                            true[nx][ny] = True
                k = Sum//cnt
                for a, b in List:
                    Map[a][b] = k
    day += 1