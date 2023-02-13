import sys
input = sys.stdin.readline
x, y = map(int,input().split())
kx, ky = map(int,input().split())


dx = [[-1,-1,-1], [-1,-1,-1], [0,-1,-1], [0,-1,-1], [0,1,1], [0,1,1], [1,1,1], [1,1,1]]
dy = [[0,-1,-1], [0,1,1], [-1,-1,-1], [1,1,1], [-1,-1,-1], [1,1,1], [0,-1,-1], [0,1,1]]

from collections import deque
queue = deque()
true = [[-1]*9 for i in range(10)]
true[x][y] = 0
queue.append([x,y])
while queue:
    x, y = queue.popleft()
    for i in range(8):
        nx, ny = x, y
        check = True
        for j in range(3):
            nx, ny = nx + dx[i][j], ny + dy[i][j]
            if 0<=nx<10 and 0<=ny<9:
                if nx == kx and ny == ky:
                    if j != 2:
                        check = False
                        break
            else:
                check = False
                break
        if check == True:
            if true[nx][ny] == -1:
                queue.append([nx,ny])
                true[nx][ny] = true[x][y]+1
                if nx == kx and ny == ky:
                    print(true[nx][ny])
                    sys.exit()
print(-1)