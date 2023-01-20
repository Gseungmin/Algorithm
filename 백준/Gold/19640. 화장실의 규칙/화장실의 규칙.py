import sys
input = sys.stdin.readline
import heapq
from collections import deque

N, M, K = map(int,input().split())
line = dict()
for i in range(N):
    d, h = map(int,input().split())
    
    num = i%M
    if num not in line:
        line[num] = deque()
        
    if i != K:
        line[num].append([-d,-h,num,1])
    else:
        line[num].append([-d,-h,num,0])

heap = []
for i in range(len(line)):
    heapq.heappush(heap, line[i].popleft())

cnt = 0
while heapq:
    x, y, k, m = heapq.heappop(heap)
    cnt += 1
    if m == 0:
        print(cnt-1)
        sys.exit()
    if len(line[k]) != 0:
        heapq.heappush(heap, line[k].popleft())