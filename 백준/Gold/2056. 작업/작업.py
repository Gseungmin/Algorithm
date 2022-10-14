import sys
input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N+1)]
time = [0]*(N+1)
ind = [0]*(N+1)
true = [0]*(N+1)
for i in range(1,N+1):
    A = list(map(int,input().split()))
    time[i] = A[0]
    ind[i] = A[1]
    if A[1] != 0:
        for j in range(2,len(A)):
            graph[A[j]].append(i)

import heapq
queue = []
for i in range(1,N+1):
    if ind[i] == 0:
        heapq.heappush(queue, [time[i], i])
        true[i] = 1
        
ans = 0
while queue:
    t, x = heapq.heappop(queue)
    ans += t
    for i in queue:
        i[0] -= t
    for nx in graph[x]:
        if true[nx] == 0:
            ind[nx] -= 1
            if ind[nx] == 0:
                heapq.heappush(queue, [time[nx], nx])
                true[nx] = 1
print(ans)