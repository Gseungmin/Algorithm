import sys
input = sys.stdin.readline
import heapq
N, M = map(int,input().split())
A, B, K, G = map(int,input().split())
if G != 0:
    visit = list(map(int,input().split())) #고둘라 방문 경로
else:
    visit = []
graph = [[] for i in range(N+1)]

Dict = dict()

for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    Dict[(a,b)] = c
    Dict[(b,a)] = c

#고둘라 경로 초기화, 즉 각 도로마다 사용하지 못하는 시간 초기화
info = dict()
time = 0
for i in range(len(visit)-1):
    x, y = visit[i], visit[i+1]
    info[(x,y)] = [time, time+Dict[(x,y)]-1]
    info[(y,x)] = [time, time+Dict[(x,y)]-1]
    time += Dict[(x,y)]

heap = []
dist = [int(1e9)]*(N+1)
true = [False]*(N+1)
dist[A] = K
heapq.heappush(heap,[dist[A], A])
while heap:
    t, x = heapq.heappop(heap) #현재 시간과 위치
    if true[x] == True:
        continue
    if x == B:
        print(t-K)
        sys.exit()
    true[x] = True
    for nx, k in graph[x]:
        if true[nx] == False: #최단 방문 시간이 확정되지 않은 경우
            if (x, nx) in info: #해당 경로가 사용못하는 경우가 있는 경우
                a, b = info[(x,nx)] #a부터 b까지 사용 불가
                if a<=t<=b: #현재 진입이 불가능하면
                    if dist[nx] > b+k+1: #b시간에 출발
                        dist[nx] = b+k+1
                        heapq.heappush(heap,[dist[nx], nx])
                else:
                    if dist[nx] > t+k: #t시간에 출발
                        dist[nx] = t+k
                        heapq.heappush(heap,[dist[nx], nx])
            else:
                if dist[nx] > t+k: #b시간에 출발
                    dist[nx] = t+k
                    heapq.heappush(heap,[dist[nx], nx])