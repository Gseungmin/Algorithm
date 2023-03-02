import sys
input = sys.stdin.readline
from collections import deque

#8:1
#판교로 돌아가야 함
#R*C 격자로 와드를 통해 좀 더 넓은 시야를 가질 수 있음
#격자의 모든 칸은 하나의 영역 안에 있는데 와드를 놓으면 해당 칸의 모든 영역을 볼 수 있음

#입력 초기화
R, C = map(int,input().split())
graph = [list(input().rstrip()) for i in range(R)]

ans = [[""]*C for i in range(R)]

#현재위치 초기화
x, y = map(int,input().split())
x, y = x-1, y-1

#명령 초기화
command = list(input().rstrip())

ward = dict()

see = dict()

dx = [-1,1,0,0,0]
dy = [0,0,-1,1,0]

direct = dict()
direct["U"] = 0
direct["D"] = 1
direct["L"] = 2
direct["R"] = 3
        
for c in command:
    
    if c == "W":
        
        #와드에 포함된 영역이 아니면
        if (x,y) not in ward:
            queue = deque()
            queue.append([x,y])
            ward[(x,y)] = True
            while queue:
                a, b = queue.popleft()
                for i in range(4):
                    na, nb = a+dx[i], b+dy[i]
                    if 0<=na<R and 0<=nb<C:
                        if graph[na][nb] == graph[x][y]:
                            if (na,nb) not in ward:
                                ward[(na,nb)] = True
                                queue.append([na,nb])
                                
    else:
        nx, ny = x+dx[direct[c]], y+dy[direct[c]]
        
        if 0<=nx<R and 0<=ny<C:
            x, y = nx, ny
        
#보기 True
for i in range(5):
    nx, ny = x+dx[i], y+dy[i]
    if 0<=nx<R and 0<=ny<C:
        see[(nx,ny)] = True
    
for i in range(R):
    for j in range(C):
        if (i,j) in ward or (i,j) in see:
            ans[i][j] = "."
        else:
            ans[i][j] = "#"

for i in ans:
    print("".join(i))