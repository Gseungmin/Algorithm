import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
dist = [[INF]*N for i in range(N)]
graph = [[] for i in range(N)]
for i in range(M):
    a, b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    dist[a-1][b-1] = 1
    dist[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

from collections import deque
queue = deque()
group = []
true = [False]*(N)
for i in range(N):
    if true[i] == False:
        case = [i]
        queue.append(i)
        true[i] = True
        while queue:
            x = queue.popleft()
            for nx in graph[x]:
                if true[nx] == False:
                    true[nx] = True
                    queue.append(nx)
                    case.append(nx)
        group.append(case)
print(len(group))
r = []
for team in group:
    L = len(team)
    ans = [-1, INF]
    for i in range(L):
        Max = 0
        for j in range(L):
            if i == j:
                continue
            Max = max(dist[team[i]][team[j]], Max)
        if ans[1] > Max:
            ans = [team[i], Max]
    r.append(ans[0])
r.sort()
for i in r:
    print(i+1)