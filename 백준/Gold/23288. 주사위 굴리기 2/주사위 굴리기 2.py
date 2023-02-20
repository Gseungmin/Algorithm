import sys
input = sys.stdin.readline
from collections import deque
N, M, K = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

#주사기 초기화
dice = dict()
dice[0] = 2
dice[1] = 1
dice[2] = 5
dice[3] = 6
dice[4] = 4
dice[5] = 3

def east():
    i, j, k, m = dice[4], dice[1], dice[5], dice[3]
    dice[4], dice[1], dice[5], dice[3] = m, i, j, k
    return

def west():
    i, j, k, m = dice[4], dice[1], dice[5], dice[3]
    dice[4], dice[1], dice[5], dice[3] = j, k, m, i
    return

def up():
    i, j, k, m = dice[0], dice[1], dice[2], dice[3]
    dice[0], dice[1], dice[2], dice[3] = j, k, m, i
    return

def down():
    i, j, k, m = dice[0], dice[1], dice[2], dice[3]
    dice[0], dice[1], dice[2], dice[3] = m, i, j, k
    return

Score = 0

x, y, k = 0, 0, 0 #초기 상황
for _ in range(K): #K번 이동하면서 로직실행

    #Condition 1
    if k == 0:
        if y == M-1:
            k = 2
            west()
            y = y-1
        else:
            east()
            y = y+1
    elif k == 1:
        if x == N-1:
            k = 3
            up()
            x = x-1
        else:
            down()
            x = x+1
    elif k == 2:
        if y == 0:
            k = 0
            east()
            y = y+1
        else:
            west()
            y = y-1
    elif k == 3:
        if x == 0:
            k = 1
            down()
            x = x+1
        else:
            up()
            x = x-1
    
    #Condition 2
    i, j = x, y
    cnt = 0
    true = [[False]*M for v in range(N)]
    queue = deque()
    queue.append([i,j])
    true[i][j] = True
    while queue:
        a, b = queue.popleft()
        cnt += 1
        for h in range(4):
            nx, ny = a+dx[h], b+dy[h]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == graph[x][y]:
                    if true[nx][ny] == False:
                        queue.append([nx,ny])
                        true[nx][ny] = True
    Score += cnt*graph[x][y]
    
    #Condition 3
    b = graph[x][y]
    a = dice[3]
    if a > b:
        k += 1
        if k == 4:
            k = 0
    elif a < b:
        k -= 1
        if k == -1:
            k = 3

print(Score)