"""
빠_늑대: x//2 -> x
여우 : x -> x*2
느_늑대: x*2 -> x*4
"""

import heapq
import sys
input = sys.stdin.readline

def dijkstra(G):
    l = len(G)-1
    dist = [float('inf')]*(l+1)
    dist[1] = 0
    H = [(0, 1)]
    
    while H:
        v, now = heapq.heappop(H)
        if dist[now] != v: continue
        
        for gv, gn in G[now]:
            if dist[gn]>gv+v:
                dist[gn] = gv+v
                heapq.heappush(H, (gv+v, gn))
    return dist            
    
    
N, M = map(int, input().split())
W = [[] for _ in range(2*N+1)]
F = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, v = map(int,input().split())
    F[a].append((2*v, b))
    F[b].append((2*v, a))
    W[a].append((v, N+b))
    W[b].append((v, N+a))
    W[N+a].append((4*v, b))
    W[N+b].append((4*v, a))
    

dis_f = dijkstra(F)
dis_w = dijkstra(W)

res= 0 
for i in range(2, N+1):
    if dis_f[i] < min(dis_w[i], dis_w[i+N]):
        res += 1
print(res)