import sys
input = sys.stdin.readline
import heapq
N = int(input())
heap = []
for _ in range(N):
    List = list(map(int,input().split()))
    if not heap:
        for num in List:
            heapq.heappush(heap,num)
    else:
        for num in List:
            if heap[0] < num:
                heapq.heappush(heap,num)
                heapq.heappop(heap)
print(heap[0])