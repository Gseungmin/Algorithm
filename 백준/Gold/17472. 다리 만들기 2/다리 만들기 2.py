import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
from collections import deque
true = [[False]*M for i in range(N)]
num = 0
Dict = dict()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and true[i][j] == False:
            true[i][j] = True
            queue = deque()
            queue.append([i,j])
            Dict[num] = []
            while queue:
                x, y = queue.popleft()
                Dict[num].append([x,y])
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<N and 0<=ny<M:
                        if graph[nx][ny] == 1 and true[nx][ny] == False:
                            true[nx][ny] = True
                            queue.append([nx,ny])
            num += 1
import heapq
heap = []
for i in range(num-1):
    for j in range(i+1,num):
        for x1, y1 in Dict[i]:
            for x2, y2 in Dict[j]:
                if x1 == x2:
                    if abs(y1-y2)-1 >= 2:
                        if y1 > y2:
                            ny = y2+1
                            check = True
                            while ny < y1:
                                if graph[x1][ny] == 1:
                                    check = False
                                    break
                                ny += 1
                        elif y1 < y2:
                            ny = y1+1
                            check = True
                            while ny < y2:
                                if graph[x1][ny] == 1:
                                    check = False
                                    break
                                ny += 1
                        if check == True:
                            heapq.heappush(heap,[abs(y1-y2)-1,i,j])
                if y1 == y2:
                    if abs(x1-x2)-1 >= 2:
                        if x1 > x2:
                            nx = x2+1
                            check = True
                            while nx < x1:
                                if graph[nx][y1] == 1:
                                    check = False
                                    break
                                nx += 1
                        elif x1 < x2:
                            nx = x1+1
                            check = True
                            while nx < x2:
                                if graph[nx][y1] == 1:
                                    check = False
                                    break
                                nx += 1
                        if check == True:
                            heapq.heappush(heap,[abs(x1-x2)-1,i,j])

UF = [i for i in range(num)]
def Find(x):
    if x == UF[x]:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y
    
def Union(x,y):
    X = Find(x)
    Y = Find(y)
    if X == Y:
        return
    if X > Y:
        UF[X] = Y
    elif X < Y:
        UF[Y] = X
    return

ans = 0
while heap:
    k, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    Union(X,Y)
    ans += k
for i in range(num):
    if UF[i] != 0 and UF[UF[i]] != 0:
        print(-1)
        sys.exit()
print(ans)