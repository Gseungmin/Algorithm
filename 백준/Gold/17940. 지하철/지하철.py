import sys
input = sys.stdin.readline
import heapq
N, M = map(int,input().split()) #M이 도착
info = [int(input()) for i in range(N)]
graph = [list(map(int,input().split())) for i in range(N)]

INF = int(1e9)
true = [[False]*N for i in range(N)]
dist = [[INF]*N for i in range(N)]
dist[0][0] = 0

heap = []
heapq.heappush(heap, [0, 0, info[0], 0]) #최소 환승횟수, 최소시간, 현재 회사, 노드
while heap:
    cnt, time, now, x = heapq.heappop(heap)
    if true[x][cnt] == True:
        continue
    if x == M:
        print(cnt, time)
        sys.exit()
    true[x][cnt] = True
    for nx in range(N):
        if graph[x][nx] == 0: #갈수 없는 경우 제외
            continue
        if now == info[nx]: #현재 회사와 같은 경우
            if true[nx][cnt] == False:
                if dist[nx][cnt] > dist[x][cnt] + graph[x][nx]:
                    dist[nx][cnt] = dist[x][cnt] + graph[x][nx]
                    heapq.heappush(heap, [cnt, dist[nx][cnt], now, nx])
        elif now != info[nx]: #현재 회사와 같지 않은 경우
            if true[nx][cnt+1] == False:
                if dist[nx][cnt+1] > dist[x][cnt] + graph[x][nx]:
                    dist[nx][cnt+1] = dist[x][cnt] + graph[x][nx]
                    heapq.heappush(heap, [cnt+1, dist[nx][cnt+1], info[nx], nx])