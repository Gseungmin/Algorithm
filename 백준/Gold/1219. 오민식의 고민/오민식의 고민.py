import sys
input = sys.stdin.readline
INF = sys.maxsize

N, s, e, M = map(int,input().split())
edge = []
graph = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    edge.append([a,b,c])

cost = list(map(int,input().split()))
dist = [-INF]*(N+1)
true = [-1]*N
from collections import deque
def BF(start):
    dist[start] = cost[start]
    queue = deque()
    for i in range(N):
        for j in edge:
            x, y, c = j[0], j[1], j[2]
            c = cost[y]-c
            if dist[x] != -INF and dist[y] < dist[x] + c:
                dist[y] = dist[x] + c
                if i == N-1:
                    true[x] = 0
                    queue.append(x)
    return queue

def isGee(queue):
    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if true[nx] == -1:
                true[nx] = 0
                queue.append(nx)
    if true[e] == 0:
        return True
    return False

ans = BF(s)
if dist[e] == -INF:
    print("gg")
else:
    if isGee(ans):
        print("Gee")
    else:
        print(dist[e])