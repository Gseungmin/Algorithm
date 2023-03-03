import sys
input = sys.stdin.readline
import heapq
n = int(input())
List = [list(map(int,input().split())) for i in range(n)]

List.sort()

heap = []

for i in List:
    heapq.heappush(heap, i[1])
    if i[0] < len(heap):
        heapq.heappop(heap)
    
print(sum(heap))