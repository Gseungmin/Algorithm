import sys
import copy
input = sys.stdin.readline
List = [list(map(int,input().split())) for i in range(3)]
from collections import deque
queue = deque()
true = dict()
arr = []
for i in range(3):
    for j in range(3):
        arr.append(List[i][j])
        if List[i][j] == 0:
            queue.append([i,j,0,copy.deepcopy(List)])
true[tuple(arr)] = 1
if (1,2,3,4,5,6,7,8,0) in true:
    print(0)
    sys.exit()
dx = [-1,1,0,0]
dy = [0,0,1,-1]
while queue:
    x, y, t, List = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<3 and 0<=ny<3:
            List[nx][ny], List[x][y] = List[x][y], List[nx][ny]
            arr = []
            for i in range(3):
                for j in range(3):
                    arr.append(List[i][j])
            arr = tuple(arr)
            if arr not in true:
                true[arr] = 1
                queue.append([nx,ny,t+1,copy.deepcopy(List)])
                if (1,2,3,4,5,6,7,8,0) in true:
                    print(t+1)
                    sys.exit()
            List[nx][ny], List[x][y] = List[x][y], List[nx][ny]
print(-1)