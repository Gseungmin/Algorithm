import sys
input = sys.stdin.readline
import heapq

#마산으로 내려갈 계획, 가장 짧은 길
#가는길에 건우가 있다면 도움을 줄 수 있음

V, E, P = map(int,input().split())

graph = [[] for i in range(V+1)]

for i in range(E):
    a, b, c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

INF = int(1e9)
dist = [INF]*(V+1)
true = [False]*(V+1)
dist[1] = 0
heap = [[0,1]]
while heap:
    k, x = heapq.heappop(heap)
    
    if true[x] == True:
        continue
    true[x] = True
    
    for nx, c in graph[x]:
        if true[nx] == False:
            if dist[nx] > dist[x] + c:
                dist[nx] = dist[x] + c
                heapq.heappush(heap, [dist[nx], nx])
                
dist2 = [INF]*(V+1)
true2 = [False]*(V+1)
dist2[P] = 0
heap = [[0,P]]
while heap:
    k, x = heapq.heappop(heap)
    
    if true2[x] == True:
        continue
    true2[x] = True
    
    for nx, c in graph[x]:
        if true2[nx] == False:
            if dist2[nx] > dist2[x] + c:
                dist2[nx] = dist2[x] + c
                heapq.heappush(heap, [dist2[nx], nx])

if dist[P] + dist2[V] == dist[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")