import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def Dijk(start):
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [0,start])
    while heap:
        t, x = heapq.heappop(heap)
        if true[x] == True:
            continue
        true[x] = True
        for nx in graph[x]:
            if true[nx] == False and dist[nx] > dist[x] + cost[(x,nx)]:
                dist[nx] = dist[x]+cost[(x,nx)]
                heapq.heappush(heap,[dist[nx], nx])
    return

from collections import deque
def BFS(start):
    queue = deque()
    queue.append(start)
    visited = set()
    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if dist[x]-dist[nx] == cost[(nx,x)] and (nx,x) not in visited:
                queue.append(nx)
                visited.add((nx,x))
    if (G,H) in visited or (H,G) in visited:
        return True
    return False
v = int(input())
for _ in range(v):
    N, M, T = map(int,input().split())
    S, G, H = map(int,input().split())
    graph = [[] for i in range(N+1)]
    cost = dict()
    for i in range(M):
        a, b, c = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        if (a,b) in cost:
            cost[(a,b)] = min(cost[(a,b)], c)
        else:
            cost[(a,b)] = c
        if (b,a) in cost:
            cost[(b,a)] = min(cost[(b,a)], c)
        else:
            cost[(b,a)] = c
    List = [int(input()) for i in range(T)]
    true = [False]*(N+1)
    dist = [INF]*(N+1)
    ans = []
    Dijk(S)
    for i in List:
        k = BFS(i)
        if k == True:
            ans.append(i)
    ans.sort()
    print(" ".join(map(str,ans)))