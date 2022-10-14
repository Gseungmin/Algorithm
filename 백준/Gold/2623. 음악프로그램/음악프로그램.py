import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().split())
true = [False]*(N+1)
ind = [0]*(N+1)
graph = [[] for i in range(N+1)]
for k in range(M):
    List = list(map(int,input().split()))
    for i in range(2,len(List)):
        graph[List[i-1]].append(List[i])
        ind[List[i]] += 1
check = N
queue = deque()
for i in range(1,N+1):
    if ind[i] == 0:
        queue.append(i)
        true[i] = True
ans = []
while queue:
    x = queue.popleft()
    ans.append(x)
    for nx in graph[x]:
        if true[nx] == False:
            ind[nx] -= 1
            if ind[nx] == 0:
                true[nx] = True
                queue.append(nx)

if len(ans) == N:
    for i in ans:
        print(i)
else:
    print(0)