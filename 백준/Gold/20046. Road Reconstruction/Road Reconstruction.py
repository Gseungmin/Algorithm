import sys
input = sys.stdin.readline
import heapq

#최소 도로 건설 비용
#7:4

#입력 초기화
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]

#절대 불가능한 경우
if graph[0][0] == -1 or graph[N-1][M-1] == -1:
    print(-1)
    sys.exit()

#이동방향 초기화
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#다익스트라 초기화
INF = int(1e9)
heap = []
true = [[False]*M for i in range(N)]
dist = [[INF]*M for i in range(N)]
dist[0][0] = graph[0][0]
heapq.heappush(heap,[dist[0][0], 0, 0])

#다익스트라 로직 시작
while heap:
    k, x, y = heapq.heappop(heap)
    
    #이미 해당 도로까지 최소 비용이 결정되었으면
    if true[x][y] == True:
        continue
    
    if x == N-1 and y == M-1:
        print(k)
        sys.exit()
    
    true[x][y] = True
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            
            if true[nx][ny] == False:
                if graph[nx][ny] == 0: #이미 도로가 있는 경우
                    if dist[nx][ny] > dist[x][y]:
                        dist[nx][ny] = dist[x][y]
                        heapq.heappush(heap, [dist[nx][ny], nx, ny])
                
                if graph[nx][ny] == 1: #도로 건설 비용이 1인 경우
                    if dist[nx][ny] > dist[x][y]+1:
                        dist[nx][ny] = dist[x][y]+1
                        heapq.heappush(heap, [dist[nx][ny], nx, ny])
                
                if graph[nx][ny] == 2: #도로 건설 비용이 2인 경경우
                    if dist[nx][ny] > dist[x][y]+2:
                        dist[nx][ny] = dist[x][y]+2
                        heapq.heappush(heap, [dist[nx][ny], nx, ny])

#도착지점에 도착하지 못할경우
print(-1)