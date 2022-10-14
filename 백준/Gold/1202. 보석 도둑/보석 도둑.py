import sys
import heapq
input = sys.stdin.readline

N, K = map(int,input().split())
jew = [list(map(int,input().split())) for i in range(N)]

for i in range(K):
    jew.append([int(input())+1,-1])
jew.sort()

ans = 0
heap = []
for i in range(N+K):
    if jew[i][1] == -1:
        if heap:
            ans += -heapq.heappop(heap)
    else:
        heapq.heappush(heap,-jew[i][1])
print(ans)