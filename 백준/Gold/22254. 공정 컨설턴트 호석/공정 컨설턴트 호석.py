import sys
input = sys.stdin.readline
N, T = map(int,input().split())
time = list(map(int,input().split()))
import heapq

def count(k):
    if k >= len(time):
        return True
    heap = []
    for i in range(k):
        heapq.heappush(heap,[time[i],i])
    index = k
    while heap:
        t, x = heapq.heappop(heap)
        if index < len(time):
            k = t+time[index]
            if k > T:
                return False
            heapq.heappush(heap,[t+time[index],index])
            index += 1
        else:
            return True
    return True

left = 1
right = N
ans = 0
while left <= right:
    mid = (left+right)//2
    if count(mid) == True:
        ans = mid
        right = mid-1
    else:
        left = mid+1
print(ans)