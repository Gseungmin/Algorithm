import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int,input().split())
graph = [list(input().rstrip()) for i in range(R)]
N = int(input())
H = list(map(int,input().split()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#막대와 부딪힌 지점 찾기
def remove(i, h):
    if i%2 == 0: #왼쪽에서 던진 경우
        for k in range(C):
            if graph[R-h][k] == "x":
                graph[R-h][k] = "."
                break
    else: #오른쪽에서 던진경우
        for k in range(C-1,-1,-1):
            if graph[R-h][k] == "x":
                graph[R-h][k] = "."
                break
    return

#중력에 의해 떨어질지 판단
def BFS(true):
    
    floor = set()
    Map = dict()
    
    cnt = 1
    for x in range(R):
        for y in range(C):
            if graph[x][y] == "x" and true[x][y] == 0:
                queue = deque()
                queue.append([x,y])
                true[x][y] = cnt
                List = []
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        nx, ny = x+dx[i], y+dy[i]
                        if i == 1: #아래 부분이 벽일 경우
                            if nx == R:
                                floor.add(cnt)
                            else:
                                if graph[nx][ny] == ".": #가장 밑 벽돌중 하나
                                    List.append([x,y])
                        if 0<=nx<R and 0<=ny<C:
                            if true[nx][ny] == 0 and graph[nx][ny] == "x":
                                true[nx][ny] = cnt
                                queue.append([nx,ny])
                if cnt not in floor:
                    Map[cnt] = List
                cnt += 1
    return [floor, Map]
        
for i in range(len(H)):
    h = H[i]
    loc_list = remove(i, h)
    
    true = [[0]*C for i in range(R)]
    floor, Map = BFS(true)

    if len(Map) == 0:
        continue
    
    new_map = dict()
    Min = 200
    for m in Map:
        for x, y in Map[m]:
            for k in range(x+1, R):
                if graph[k][y] == "x":
                    if true[k][y] == true[x][y]: #같은 벽돌이면
                        break
                    else: #내려갈 수 있는 벽돌
                        Min = min(Min, k-x-1)
                        break
                elif graph[k][y] == "." and k == R-1: #맨 아래 벽돌까지 추락할 수 있으면
                    Min = min(Min, k-x)
                    break
        new_map[m] = Min
    
    for x in range(R):
        for y in range(C):
            if true[x][y] in new_map:
                graph[x][y] = "."
    
    for x in range(R):
        for y in range(C):
            if true[x][y] in new_map:
                graph[x+new_map[true[x][y]]][y] = "x"
                
for i in graph:
    print("".join(i))