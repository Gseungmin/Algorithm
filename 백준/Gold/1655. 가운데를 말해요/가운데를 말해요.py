import sys
input = sys.stdin.readline
N = int(input())
import heapq
left = []
right = []
ans = []
for i in range(N):
    k = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -k)
    else:
        heapq.heappush(right, k)
    if right and -left[0] > right[0]:
        a = -heapq.heappop(left)
        b = heapq.heappop(right)
        heapq.heappush(left, -b)
        heapq.heappush(right, a)
    ans.append(-left[0])
for i in ans:
    print(i)