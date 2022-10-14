import sys
input = sys.stdin.readline
from collections import deque
R, C, K = map(int,input().split()) #R과 C는 행과 열, K 조사하는 모든 칸의 온도
graph = [list(map(int,input().split())) for i in range(R)] #현재 상태
temper = [[0]*C for i in range(R)]
machine = dict()
check = dict()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(R):
    for j in range(C):
        if graph[i][j] == 5:
            check[(i,j)] = True
        elif graph[i][j] != 0:
            machine[(i,j)] = graph[i][j]
W = int(input()) #조사해야하는 벽돌의 수
brick = dict()
for i in range(W):
    x, y, t = map(int,input().split())
    x, y = x-1, y-1
    if t == 0:
        brick[(x,y,x-1,y)] = True
        brick[(x-1,y,x,y)] = True
    else:
        brick[(x,y,x,y+1)] = True
        brick[(x,y+1,x,y)] = True
chocolate = 0
while chocolate <= 100:
    #단계1 기계를 통한 온도 조절
    for i, j in machine:
        k = machine[(i,j)]
        queue = deque()
        true = set()
        if k == 1: #온풍기 방향이 오른쪽일 경우
            queue.append([i,j+1,1])
            true.add((i,j+1))
            temper[i][j+1] += 5
            while queue:
                x, y, t = queue.popleft()
                if t == 5:
                    break
                if x-1 >= 0 and y+1 < C: #범위 만족할때
                    if (x-1,y+1) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x-1,y) not in brick and (x-1,y,x-1,y+1) not in brick:
                            queue.append([x-1,y+1,t+1])
                            true.add((x-1,y+1))
                            temper[x-1][y+1] += (5-t)
                if x+1 < R and y+1 < C: #범위 만족할때
                    if (x+1,y+1) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x+1,y) not in brick and (x+1,y,x+1,y+1) not in brick:
                            queue.append([x+1,y+1,t+1])
                            true.add((x+1,y+1))
                            temper[x+1][y+1] += (5-t)
                if y+1 < C: #범위 만족할때
                    if (x,y+1) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x,y+1) not in brick:
                            queue.append([x,y+1,t+1])
                            true.add((x,y+1))
                            temper[x][y+1] += (5-t)
        elif k == 2: #온풍기 방향이 왼쪽일 경우
            queue.append([i,j-1,1])
            true.add((i,j-1))
            temper[i][j-1] += 5
            while queue:
                x, y, t = queue.popleft()
                if t == 5:
                    break
                if x-1 >= 0 and y-1 >= 0: #범위 만족할때
                    if (x-1,y-1) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x-1,y) not in brick and (x-1,y,x-1,y-1) not in brick:
                            queue.append([x-1,y-1,t+1])
                            true.add((x-1,y-1))
                            temper[x-1][y-1] += (5-t)
                if x+1 < R and y-1 >= 0: #범위 만족할때
                    if (x+1,y-1) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x+1,y) not in brick and (x+1,y,x+1,y-1) not in brick:
                            queue.append([x+1,y-1,t+1])
                            true.add((x+1,y-1))
                            temper[x+1][y-1] += (5-t)
                if y-1 >= 0:#범위 만족할때
                    if (x,y-1) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x,y-1) not in brick:
                            queue.append([x,y-1,t+1])
                            true.add((x,y-1))
                            temper[x][y-1] += (5-t)
        elif k == 3: #온풍기 방향이 위쪽일 경우
            queue.append([i-1,j,1])
            true.add((i-1,j))
            temper[i-1][j] += 5
            while queue:
                x, y, t = queue.popleft()
                if t == 5:
                    break
                if x-1 >= 0 and y-1 >= 0: #범위 만족할때
                    if (x-1,y-1) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x,y-1) not in brick and (x,y-1,x-1,y-1) not in brick:
                            queue.append([x-1,y-1,t+1])
                            true.add((x-1,y-1))
                            temper[x-1][y-1] += (5-t)
                if x-1 >= 0 and y+1 < C: #범위 만족할때
                    if (x-1,y+1) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x,y+1) not in brick and (x,y+1,x-1,y+1) not in brick:
                            queue.append([x-1,y+1,t+1])
                            true.add((x-1,y+1))
                            temper[x-1][y+1] += (5-t)
                if x-1 >= 0: #범위 만족할때
                    if (x-1,y) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x-1,y) not in brick:
                            queue.append([x-1,y,t+1])
                            true.add((x-1,y))
                            temper[x-1][y] += (5-t)
        elif k == 4: #온풍기 방향이 아래쪽일 경우
            queue.append([i+1,j,1])
            true.add((i+1,j))
            temper[i+1][j] += 5
            while queue:
                x, y, t = queue.popleft()
                if t == 5:
                    break
                if x+1 < R and y+1 < C: #범위 만족할때
                    if (x+1,y+1) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x,y+1) not in brick and (x,y+1,x+1,y+1) not in brick:
                            queue.append([x+1,y+1,t+1])
                            true.add((x+1,y+1))
                            temper[x+1][y+1] += (5-t)
                if x+1 < R and y-1 >= 0: #범위 만족할때
                    if (x+1,y-1) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x,y-1) not in brick and (x,y-1,x+1,y-1) not in brick:
                            queue.append([x+1,y-1,t+1])
                            true.add((x+1,y-1))
                            temper[x+1][y-1] += (5-t)
                if x+1 < R: #범위 만족할때
                    if (x+1,y) not in true: #온도 변화가 아직 안 일어났을 때
                        if (x,y,x+1,y) not in brick:
                            queue.append([x+1,y,t+1])
                            true.add((x+1,y))
                            temper[x+1][y] += (5-t)
    #단계 2 온도 조절
    value = dict()
    for x in range(R):
        for y in range(C):
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<R and 0<=ny<C:
                    if (x,y,nx,ny) not in brick: #온도 조절이 가능한 경우
                        if temper[x][y] > temper[nx][ny]: #온도가 더 큰 경우
                            v = (temper[x][y]-temper[nx][ny])//4
                            value[(x,y,nx,ny)] = v
    for x, y, nx, ny in value: #온도 조절이 필요한 곳 조절
        k = value[(x,y,nx,ny)]
        temper[x][y] -= k
        temper[nx][ny] += k
    #단계 3 바깥쪽 온도 조절
    for i in range(C):
        temper[0][i] = max(0, temper[0][i]-1)
        temper[R-1][i] = max(0, temper[R-1][i]-1)
    for i in range(1,R-1):
        temper[i][0] = max(0, temper[i][0]-1)
        temper[i][C-1] = max(0, temper[i][C-1]-1)
    #단계 4 초콜릿 먹기
    chocolate += 1
    #단계 5 온도 check
    ans = True
    for i, j in check:
        if temper[i][j] < K:
            ans = False
            break
    if ans == True:
        print(chocolate)
        sys.exit()
print(101)