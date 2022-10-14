import sys
input = sys.stdin.readline
N, K = map(int,input().split())
L = [int(input()) for i in range(N)]
left = min(L)
right = max(L)+K
ans = 0
while left <= right:
    mid = (left+right)//2
    cnt = 0
    check = 0
    for i in L:
        if i < mid:
            cnt += mid-i
            if cnt > K:
                check = 1
    if check == 0:
        ans = mid
        left = mid+1
    else:
        right = mid-1
print(ans)