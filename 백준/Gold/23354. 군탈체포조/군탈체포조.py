import sys
input = sys.stdin.readline
N = int(input())
List = [list(map(int,input().split())) for i in range(N)]
gate = []
center = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
for i in range(N):
    for j in range(N):
        if List[i][j] == 0:
            gate.append([i,j])
        elif List[i][j] == -1:
            center.append([i,j])
            List[i][j] = 0
if len(gate) == 0:
    print(0)
    sys.exit()
cost = dict()
import heapq
INF = int(1e9)
def Dijk(a,b):
    true = [[False]*N for i in range(N)]
    dist = [[INF]*N for i in range(N)]
    dist[a][b] = 0
    heap = []
    heapq.heappush(heap, [0,a,b])
    check = 0
    while heap:
        t, x, y = heapq.heappop(heap)
        if true[x][y] == True:
            continue
        true[x][y] = True
        if List[x][y] == 0:
            check += 1
            if check == len(gate)+1:
                break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if true[nx][ny] == False:
                    if dist[nx][ny] > dist[x][y] + List[nx][ny]:
                        dist[nx][ny] = dist[x][y] + List[nx][ny]
                        heapq.heappush(heap,[dist[nx][ny], nx, ny])
    for x, y in gate:
        if x == a and y == b:
            continue
        cost[(a,b,x,y)] = dist[x][y]
    cost[(a,b,center[0][0], center[0][1])] = dist[center[0][0]][center[0][1]]
    cost[(a,b,center[0][0], center[0][1])] = dist[center[0][0]][center[0][1]]
    return
for a, b in gate:
    Dijk(a,b)
K = len(gate)
import itertools
gate = itertools.permutations(gate)
Min = INF
for case in gate:
    x, y = center[0][0], center[0][1]
    time = cost[(case[0][0], case[0][1], x, y)] + cost[(case[-1][0], case[-1][1], x, y)]
    for i in range(K-1):
        time += cost[(case[i][0], case[i][1], case[i+1][0], case[i+1][1])]
    Min = min(Min,time)
print(Min)