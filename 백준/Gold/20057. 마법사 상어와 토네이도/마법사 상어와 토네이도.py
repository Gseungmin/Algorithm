import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
cx, cy = N//2, N//2

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def left(x,y):
    List = []
    List.append([x-1,y+1,1])
    List.append([x+1,y+1,1])
    List.append([x-1,y,7])
    List.append([x+1,y,7])
    List.append([x-2,y,2])
    List.append([x+2,y,2])
    List.append([x-1,y-1,10])
    List.append([x+1,y-1,10])
    List.append([x,y-2,5])
    List.append([x,y-1,0])
    return List

def right(x,y):
    List = []
    List.append([x-1,y-1,1])
    List.append([x+1,y-1,1])
    List.append([x-1,y,7])
    List.append([x+1,y,7])
    List.append([x-2,y,2])
    List.append([x+2,y,2])
    List.append([x-1,y+1,10])
    List.append([x+1,y+1,10])
    List.append([x,y+2,5])
    List.append([x,y+1,0])
    return List

def up(x,y):
    List = []
    List.append([x+1,y+1,1])
    List.append([x+1,y-1,1])
    List.append([x,y+1,7])
    List.append([x,y-1,7])
    List.append([x,y+2,2])
    List.append([x,y-2,2])
    List.append([x-1,y+1,10])
    List.append([x-1,y-1,10])
    List.append([x-2,y,5])
    List.append([x-1,y,0])
    return List
    
def down(x,y):
    List = []
    List.append([x-1,y+1,1])
    List.append([x-1,y-1,1])
    List.append([x,y+1,7])
    List.append([x,y-1,7])
    List.append([x,y+2,2])
    List.append([x,y-2,2])
    List.append([x+1,y+1,10])
    List.append([x+1,y-1,10])
    List.append([x+2,y,5])
    List.append([x+1,y,0])
    return List

#토네이도 경로    
route = []
from collections import deque
queue = deque()
true = dict()
true[(0,0)] = True
queue.append([0,0,0])
while queue:
    x, y, k = queue.popleft()
    route.append([x,y])
    if x == cx and y == cy:
        break
    check = False
    nx, ny = x+dx[k], y+dy[k]
    if 0<=nx<N and 0<=ny<N:
        if (nx,ny) not in true:
            queue.append([nx,ny,k])
            true[(nx,ny)] = True
            check = True
    if check == False:
        k += 1
        if k == 4:
            k = 0
        nx, ny = x+dx[k], y+dy[k]
        queue.append([nx,ny,k])
        true[(nx,ny)] = True

Sum = 0
route = deque(route[::-1])

while route:
    x, y = route.popleft()
    if x == 0 and y == 0:
        break
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if route[0][0] == nx and route[0][1] == ny: #경로가 맞을 시
            if i == 0:
                arr = right(nx,ny)
            elif i == 1:
                arr = down(nx,ny)
            elif i == 2:
                arr = left(nx,ny)
            else:
                arr = up(nx,ny)
            if graph[nx][ny] != 0:
                In = 0 
                Out = 0
                for a, b, c in arr:
                    if c != 0:
                        if 0<=a<N and 0<=b<N:
                            graph[a][b] += graph[nx][ny]*c//100
                            In += graph[nx][ny]*c//100
                        else:
                            Out += graph[nx][ny]*c//100
                    else:
                        if 0<=a<N and 0<=b<N:
                            graph[a][b] += graph[nx][ny]-(In+Out)
                            Sum += Out
                        else:
                            Sum += (graph[nx][ny]-In)
                graph[nx][ny] = 0

print(Sum)