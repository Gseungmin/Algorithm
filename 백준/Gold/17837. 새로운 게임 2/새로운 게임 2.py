import sys
input = sys.stdin.readline
N, K = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
horse = dict()
height = dict()
for i in range(N):
    for j in range(N):
        height[(i,j)] = []
for i in range(K):
    a,b,c = map(int,input().split())
    horse[i] = [a-1,b-1,c-1]
    height[(a-1,b-1)].append(i)

from collections import deque
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for t in range(1,1001):
    for n in range(K):
        x, y, d = horse[n]
        nx, ny = x+dx[d], y+dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] == 2:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
            nx, ny = x+dx[d], y+dy[d]
            horse[n][2] = d
        if 0<=nx<N and 0<=ny<N and graph[nx][ny] != 2:
            if graph[nx][ny] == 0:
                List = deque()
                while 1:
                    k = height[(x,y)].pop()
                    List.appendleft(k)
                    horse[k][0] = nx
                    horse[k][1] = ny
                    if k == n:
                        break
                List = list(List)
                height[(nx,ny)] += List
                if len(height[nx,ny]) >= 4:
                    print(t)
                    sys.exit()
            elif graph[nx][ny] == 1:
                List = deque()
                while 1:
                    k = height[(x,y)].pop()
                    List.append(k)
                    horse[k][0] = nx
                    horse[k][1] = ny
                    if k == n:
                        break
                List = list(List)
                height[(nx,ny)] += List
                if len(height[nx,ny]) >= 4:
                    print(t)
                    sys.exit()
print(-1)