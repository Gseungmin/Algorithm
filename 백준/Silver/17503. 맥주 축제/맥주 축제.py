import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
heap = []
for i in range(K):
    v, c = map(int,input().split())
    heap.append([-v,c])
heap.sort()
ans = -1
left = 1
right = 2**31-1
while left <= right:
    mid = (left+right)//2
    Sum = 0
    check = 0
    day = 0
    for i, j in heap:
        if j <= mid:
            day += 1
            Sum += -i
        if Sum >= M and day == N:
            check = 1
            break
    if check == 0:
        left = mid+1
    else:
        ans = mid
        right = mid-1
print(ans)