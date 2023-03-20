import sys
import heapq
def solution(board):
    heap = []
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    N = len(board)
    INF = int(1e9)
    true = [[[False]*4 for i in range(N)] for j in range(N)]
    dist = [[[INF]*4 for i in range(N)] for j in range(N)]
    heapq.heappush(heap,[0,0,0,2])
    heapq.heappush(heap,[0,0,0,1])
    dist[0][0][2] = 0
    dist[0][0][1] = 0
    while heapq:
        k, x, y, d = heapq.heappop(heap)
        if true[x][y][d] == True:
            continue
        if x == N-1 and y == N-1:
            return k
        true[x][y][d] = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] == 0:
                    if d == i:
                        if true[nx][ny][d] == False:
                            if dist[nx][ny][d] > dist[x][y][d] + 100:
                                dist[nx][ny][d] = dist[x][y][d] + 100
                                heapq.heappush(heap, [dist[nx][ny][d], nx, ny, d])
                    elif abs(d-i) == 1 or abs(d-i) == 3:
                        if true[nx][ny][d] == False:
                            if dist[nx][ny][i] > dist[x][y][d] + 600:
                                dist[nx][ny][i] = dist[x][y][d] + 600
                                heapq.heappush(heap, [dist[nx][ny][i], nx, ny, i])
    return 0