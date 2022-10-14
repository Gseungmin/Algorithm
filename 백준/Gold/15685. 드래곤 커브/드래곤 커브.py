import sys
input = sys.stdin.readline
N = int(input())
dx = [1,0,-1,0]
dy = [0,-1,0,1]
Dict = dict()
from collections import deque
for i in range(N):
    cnt = 0
    x, y, d, g = map(int,input().split())
    nx, ny = x+dx[d], y+dy[d]
    Dict[(x,y)] = True
    Dict[(nx,ny)] = True
    queue = deque()
    queue.append([nx,ny,[d]])
    while cnt < g:
        x, y, d_list = queue.popleft()
        nd_list = d_list.copy()
        while d_list:
            d = d_list.pop()
            nd = (d+1)%4
            nx, ny = x+dx[nd], y+dy[nd]
            Dict[(x,y)] = True
            Dict[(nx,ny)] = True
            nd_list.append(nd)
            x, y = nx, ny
        cnt += 1
        queue.append([x,y,nd_list])
ans = 0
for i in range(100):
    for j in range(100):
        if (i,j) in Dict and (i+1,j) in Dict and (i,j+1) in Dict and (i+1,j+1) in Dict:
            ans += 1
print(ans)