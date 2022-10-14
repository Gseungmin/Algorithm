import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
left = 0
right = 200
dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque
def BFS(Min, Max):
    if graph[0][0] > Max or graph[0][0] < Min:
        return False
    queue = deque()
    queue.append([0,0])
    true = [[False]*N for i in range(N)]
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == N-1:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if true[nx][ny] == False:
                    if graph[nx][ny] > Max or graph[nx][ny] < Min:
                        continue
                    true[nx][ny] = True
                    queue.append([nx,ny])
    return False
    
ans = 0
while left <= right:
    mid = (left+right)//2
    check = 0
    for i in range(200-mid+1):
        if BFS(i,i+mid):
            check = 1
            break
    if check == 1:
        ans = mid
        right= mid-1
    else:
        left = mid+1
print(ans)