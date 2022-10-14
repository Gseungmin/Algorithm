N = int(input())
graph = [list(input()) for i in range(N)]
door = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == '#':
            door.append([i,j])
true = [[[-1]*4 for i in range(N)] for j in range(N)]
from collections import deque
queue = deque()
a, b = door.pop()
e, f = door.pop()
graph[e][f] = '!'
queue.append([a,b,0])
queue.append([a,b,1])
queue.append([a,b,2])
queue.append([a,b,3])
true[a][b][0] = 0
true[a][b][1] = 0
true[a][b][2] = 0
true[a][b][3] = 0
while queue:
    x, y, d = queue.popleft()
    if x == e and y == f:
        print(true[x][y][d]-1)
        exit()
    if d == 0:
        index = 1
        while x-index >= 0:
            if graph[x-index][y] == '*':
                break
            if graph[x-index][y] == '!':
                if true[x-index][y][1] == -1:
                    true[x-index][y][1] = true[x][y][d] + 1
                    queue.append([x-index,y,1])
                if true[x-index][y][3] == -1:
                    true[x-index][y][3] = true[x][y][d] + 1
                    queue.append([x-index,y,3])
            index += 1
    if d == 1:
        index = 1
        while y+index < N:
            if graph[x][y+index] == '*':
                break
            if graph[x][y+index] == '!':
                if true[x][y+index][0] == -1:
                    true[x][y+index][0] = true[x][y][d] + 1
                    queue.append([x,y+index,0])
                if true[x][y+index][2] == -1:
                    true[x][y+index][2] = true[x][y][d] + 1
                    queue.append([x,y+index,2])
            index += 1
    if d == 2:
        index = 1
        while x+index < N:
            if graph[x+index][y] == '*':
                break
            if graph[x+index][y] == '!':
                if true[x+index][y][1] == -1:
                    true[x+index][y][1] = true[x][y][d] + 1
                    queue.append([x+index,y,1])
                if true[x+index][y][3] == -1:
                    true[x+index][y][3] = true[x][y][d] + 1
                    queue.append([x+index,y,3])
            index += 1
    if d == 3:
        index = 1
        while y-index >= 0:
            if graph[x][y-index] == '*':
                break
            if graph[x][y-index] == '!':
                if true[x][y-index][0] == -1:
                    true[x][y-index][0] = true[x][y][d] + 1
                    queue.append([x,y-index,0])
                if true[x][y-index][2] == -1:
                    true[x][y-index][2] = true[x][y][d] + 1
                    queue.append([x,y-index,2])
            index += 1