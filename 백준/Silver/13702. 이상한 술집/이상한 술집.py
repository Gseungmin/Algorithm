import sys
input = sys.stdin.readline
N, K = map(int,input().split())
List = [int(input()) for i in range(N)]
left = 1
right = max(List)
ans = 1
while left <= right:
    mid = (left+right)//2
    cnt = 0
    for i in List:
        cnt += i//mid
    if cnt >= K:
        ans = mid
        left = mid+1
    else:
        right = mid-1
print(ans)