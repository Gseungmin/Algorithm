import sys
input = sys.stdin.readline
N = int(input()) #size
x1, y1, x2, y2 = map(int,input().split())
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
dist = []
for i in range(N):
    dist.append([-1]*N)
    
from collections import deque

def knight(x1,y1,x2,y2,dist):
    queue = deque()
    queue.append([x1,y1])
    dist[x1][y1] = 0
    while queue:
        a, b = queue.popleft()
        for i in range(6):
            c = a + dx[i]
            d = b + dy[i]
            if 0<=c<N and 0<=d<N:
                if dist[c][d] == -1: #방문한 적이 없다면
                    queue.append([c,d])
                    dist[c][d] = dist[a][b] + 1
                    if c == x2 and d == y2:
                        print(dist[c][d])
                        return
    print(-1)
    return

knight(x1,y1,x2,y2,dist)