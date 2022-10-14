import sys
input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N+1)]
cost = [0]*(N+1)
ind = [0]*(N+1)
true = [-1]*(N+1)
for i in range(1,N+1):
    arr = list(map(int,input().split()))
    cost[i] = arr[0]
    for j in range(1,len(arr)):
        if arr[j] == -1:
            break
        ind[i] += 1
        graph[arr[j]].append(i)

ans = [0]*(N+1)
import heapq
heap = []
for i in range(1,N+1):
    if ind[i] == 0:
        heapq.heappush(heap,[cost[i],i])
        true[i] = 0
k = 0
while heap:
    t, x = heapq.heappop(heap)
    k += t
    ans[x] = k
    for i in heap:
        i[0] -= t
    for nx in graph[x]:
        if true[nx] == -1:
            ind[nx] -= 1
            if ind[nx] == 0:
                heapq.heappush(heap,[cost[nx],nx])
                true[nx] = 0
for i in range(1,N+1):
	print(ans[i])