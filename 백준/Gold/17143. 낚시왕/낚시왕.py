import sys
input = sys.stdin.readline
import heapq
import copy
R, C, W = map(int,input().split())
graph = dict()
for i in range(R):
    for j in range(C):
        graph[(i,j)] = []
fish = dict()
for i in range(W):
    r, c, speed, direct, size = map(int,input().split())
    fish[i] = [speed,direct,size,r-1,c-1]
    heapq.heappush(graph[(r-1,c-1)],[size,i])
index = 0
ans = 0
while index < C:
    for i in range(R):
        if len(graph[(i,index)]) == 1:
            k = heapq.heappop(graph[(i,index)])[1]
            ans += fish[k][2]
            fish.pop(k)
            break
    new_graph = dict()
    for i in range(R):
        for j in range(C):
            new_graph[(i,j)] = []
    for i in fish:
        speed, direct, size, x, y = fish[i]
        v = speed
        nx, ny = x, y
        while 1:
            if direct == 1:
                if nx == v:
                    nx = 0
                    break
                elif nx > v:
                    nx -= v
                    break
                elif nx < v:
                    v -= nx
                    nx = 0
                    direct = 2
            elif direct == 2:
                if nx + v == R-1:
                    nx = R-1
                    break
                elif nx + v < R-1:
                    nx += v
                    break
                elif nx + v > R-1:
                    v -= (R-1-nx)
                    nx = R-1
                    direct = 1
            elif direct == 4:
                if ny == v:
                    ny = 0
                    break
                elif ny > v:
                    ny -= v
                    break
                elif ny < v:
                    v -= ny
                    ny = 0
                    direct = 3
            elif direct == 3:
                if ny + v == C-1:
                    ny = C-1
                    break
                elif ny + v < C-1:
                    ny += v
                    break
                elif ny + v > C-1:
                    v -= (C-1-ny)
                    ny = C-1
                    direct = 4
        fish[i][1], fish[i][3], fish[i][4] = direct, nx, ny
        heapq.heappush(new_graph[(nx,ny)],[size,i])
    for i in range(R):
        for j in range(C):
            while len(new_graph[(i,j)]) >= 2:
                k = heapq.heappop(new_graph[(i,j)])
                fish.pop(k[1])
    graph = copy.deepcopy(new_graph)
    index += 1
print(ans)