import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []
for i in range(N):
    heapq.heappush(heap,int(input()))

if N == 1:
    print(0)
    sys.exit()
    
stack = []
ans = 0
while heapq:
    if len(heap) == 1:
        print(heap[0] + ans)
        break
    if not stack:
        a = heapq.heappop(heap)
        stack.append(a)
        ans += a
    else:
        a = stack.pop()
        b = heapq.heappop(heap)
        ans += b
        heapq.heappush(heap, a+b)