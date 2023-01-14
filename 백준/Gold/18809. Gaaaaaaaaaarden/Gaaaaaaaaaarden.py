import sys
input = sys.stdin.readline
N, M, G, R = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]

pos = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            pos.append([i,j])

from itertools import combinations
import copy
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

green = list(combinations(pos,G))
ans = 0
total = 0
for i in range(len(green)):
    green_dict = dict()
    for j in green[i]:
        green_dict[tuple(j)] = True
    remain = []
    for j in pos:
        if tuple(j) not in green_dict: 
            remain.append(j)
    red = list(combinations(remain,R))
    # green은 정해졌고 red는 그에 따른 모든 케이스를 가지고 옴
    for case in red:
        total += 1
        flower = dict()
        queue = deque()
        true = [[0]*M for _ in range(N)]
        dist = [[0]*M for _ in range(N)]
        for x, y in green[i]:
            true[x][y] = 1 #green = 1
            queue.append([x,y,1])
        for x, y in case:
            true[x][y] = 2 #red = 2
            queue.append([x,y,2])
        while queue:
            x, y, k = queue.popleft()
            if (x,y) in flower: #꽃이 되어버렸으면 이동 불가능
                continue
            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]
                if 0<=nx<N and 0<=ny<M:
                    if graph[nx][ny] == 0: #호수 위치면
                        continue
                    if true[nx][ny] == 0: #해당 위치에 배양액이 없으면
                        true[nx][ny] = k
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append([nx,ny,k])
                    else: #해당 위치에 배양액이 있으면
                        if true[nx][ny] != true[x][y]: #꽃이 될 가능성이 있음
                            if dist[nx][ny] == dist[x][y]+1:
                                flower[(nx,ny)] = True
        ans = max(ans, len(flower))
print(ans)