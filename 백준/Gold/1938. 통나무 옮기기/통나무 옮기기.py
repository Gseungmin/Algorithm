import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(input().rstrip()) for i in range(N)]

ref = []
for i in range(N):
    for j in range(N):
        ref.append([i,j])


tree = dict()
now = []
des = dict()

for i in range(N):
    for j in range(N):
        if graph[i][j] == "1":
            tree[(i,j)] = True
        if graph[i][j] == "B":
            now.append([i,j])
        if graph[i][j] == "E":
            des[(i,j)] = True
            graph[i][j] = "0"
now.sort()
status = 1 #verti
if now[0][1]+1 == now[1][1]:
    status = 0 #horiz
    
ans = [int(1e9)]

true = dict()

queue = deque()
queue.append([now, status, 0])
while queue:
    now, status, count = queue.popleft()
    
    #중복 검사
    case = []
    for q, w in now:
        case.append(q)
        case.append(w)
    if tuple(case) in true:
        continue
    true[tuple(case)] = True
    
    #현재 위치와 목적지 위치 대조, 맞다면 결과 출력
    total = 0
    for a, b in now:
        if (a,b) in des:
            total += 1
    if total == 3:
        print(count)
        sys.exit()
    
    if status == 0:
        #hor_up
        hor_up = []
        for i in range(3):
            x, y = now[i][0], now[i][1]
            nx = x-1
            if nx >= 0 and graph[nx][y] != "1":
                hor_up.append([nx, y])
        if len(hor_up) == 3:
            queue.append([hor_up, status, count+1])
                    
        #hor_down
        hor_down = []
        for i in range(3):
            x, y = now[i][0], now[i][1]
            nx = x+1
            if nx < N and graph[nx][y] != "1":
                hor_down.append([nx, y])
        if len(hor_down) == 3:
            queue.append([hor_down, status, count+1])
                    
        #hor_right
        hor_right = []
        x, y = now[2][0], now[2][1]+1
        if y < N and graph[x][y] != "1":
            hor_right = [[x,y-2],[x,y-1],[x,y]]
            queue.append([hor_right, status, count+1])
        
        #hor_left
        hor_left = []
        x, y = now[0][0], now[0][1]-1
        if y >= 0 and graph[x][y] != "1":
            hor_left = [[x,y],[x,y+1],[x,y+2]]
            queue.append([hor_left, status, count+1])
            
        #trun
        x, y = now[1][0], now[1][1]
        check = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if 0<=i<N and 0<=j<N:
                    if graph[i][j] != "1":
                        check += 1
        if check == 9:
            hor_turn = [[x-1,y],[x,y],[x+1,y]]
            queue.append([hor_turn, 1, count+1])
    
    elif status == 1:
        
        #ver_left
        ver_left = []
        for i in range(3):
            x, y = now[i][0], now[i][1]
            ny = y-1
            if ny >= 0 and graph[x][ny] != "1":
                ver_left.append([x, ny])
        if len(ver_left) == 3:
            queue.append([ver_left, status, count+1])
                    
        #ver_right
        ver_right = []
        for i in range(3):
            x, y = now[i][0], now[i][1]
            ny = y+1
            if ny < N and graph[x][ny] != "1":
                ver_right.append([x, ny])
        if len(ver_right) == 3:
            queue.append([ver_right, status, count+1])

        #ver_down
        ver_down = []
        x, y = now[2][0]+1, now[2][1]
        if x < N and graph[x][y] != "1":
            ver_down = [[x-2,y],[x-1,y],[x,y]]
            queue.append([ver_down, status, count+1])
        
        #ver_up
        ver_up = []
        x, y = now[0][0]-1, now[0][1]
        if x >= 0 and graph[x][y] != "1":
            ver_up = [[x,y],[x+1,y],[x+2,y]]
            queue.append([ver_up, status, count+1])
            
        #trun
        x, y = now[1][0], now[1][1]
        check = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if 0<=i<N and 0<=j<N:
                    if graph[i][j] != "1":
                        check += 1
        if check == 9:
            ver_turn = [[x,y-1],[x,y],[x,y+1]]
            queue.append([ver_turn, 0, count+1])

print(0)