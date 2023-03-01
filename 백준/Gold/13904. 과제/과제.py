import sys
input = sys.stdin.readline
import heapq

#가장 많은 점수, 하루에 한 과제
#12:25

#60
N = int(input())

heap = []
for i in range(N):
    a, b = map(int,input().split())
    heapq.heappush(heap,[-b,a])
    
pos = [0]*(1000)
Sum = 0
while heap:
    x, y = heapq.heappop(heap)
    for j in range(y-1,-1,-1):
        if pos[j] == 0:
            pos[j] += 1
            Sum += -x
            break
print(Sum)