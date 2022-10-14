import sys
input = sys.stdin.readline
T, N = map(int,input().split())
import heapq
heap = []
for i in range(N):
    a, b, c = map(int,input().split())  
    heapq.heappush(heap,[-c,a,b])

ans = []
for _ in range(T):
    c, a, b = heapq.heappop(heap)
    b -= 1
    ans.append(a)
    if b != 0:
        heapq.heappush(heap, [c+1,a,b])

for i in range(T):
    sys.stdout.write(str(ans[i])+'\n')