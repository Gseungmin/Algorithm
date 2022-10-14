import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int,input().split())
edge = []
graph = [[] for i in range(N+1)]
graph_r = [[] for i in range(N+1)]
cost = dict()
for i in range(M):
    a, b, c = map(int,input().split())
    edge.append([a,b,c])
    graph[b].append(a)
    graph_r[a].append(b)
    if (b,a) not in cost:
        cost[(b,a)] = c
    else:
        cost[(b,a)] = max(cost[(b,a)],c)

from collections import deque
def BF():
    queue = deque()
    dist[1] = 0
    true2 = [False]*(N+1)
    check = 0
    for i in range(N):
        for j in edge:
            s, e, k = j[0], j[1], j[2]
            if dist[s] != -INF and dist[e] < dist[s] + k:
                dist[e] = dist[s] + k
                if i == N-1:
                    check = 1
                    queue.append(s)
                    true2[s] = True
    if check == 0:
        return True
    while queue:
        x = queue.popleft()
        for nx in graph_r[x]:
            if true2[nx] == False:
                true2[nx] = True
                queue.append(nx)
    if true2[N] == True:
        return False
    return True
dist = [-INF]*(N+1)
ans = BF()
List = [N]
true = [False]*(N+1)
true[N] = True
def DFS(x):
    if x == 1:
        print(" ".join(map(str,List[::-1])))
        sys.exit()
    for nx in graph[x]:
        if true[nx] == False and dist[x]-dist[nx] == cost[(x,nx)]:
            true[nx] = True
            List.append(nx)
            DFS(nx)
            true[nx] = False
            List.pop()
    return

if ans == False or dist[N] == -INF:
    print(-1)
else:
    DFS(N)