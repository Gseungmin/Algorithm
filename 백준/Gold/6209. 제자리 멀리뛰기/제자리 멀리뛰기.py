import sys
input = sys.stdin.readline

d, n, m = map(int,input().split())
if n == m or n == 0:
    print(d)
    sys.exit()

dist = [int(input()) for i in range(n)] + [0, d]
dist.sort()
left = 0
right = dist[-1]
L = len(dist)
ans = 0

while left <= right:
    mid = (left+right)//2
    check = False
    cnt = 0
    x = 0
    nx = 1
    while x < L and nx < L:
        if dist[nx] - dist[x] == mid:
            check = True
            cnt += 1
            x = nx
            nx = x+1
        elif dist[nx] - dist[x] > mid:
            cnt += 1
            x = nx
            nx = x+1
        elif dist[nx] - dist[x] < mid:
            nx += 1
    
    if cnt >= (n-m+1):
        left = mid+1
        if check == True:
            ans = mid
    else:
        right = mid-1
    
print(ans)