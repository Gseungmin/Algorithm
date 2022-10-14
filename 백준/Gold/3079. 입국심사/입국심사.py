import sys
input = sys.stdin.readline
N, M = map(int,input().split())
List = [int(input()) for i in range(N)]
left = 1
right = sys.maxsize
ans = 0
while left <= right:
    mid = (left+right)//2
    cnt = 0
    pos = False
    for i in List:
        cnt += mid//i
        if cnt >= M:
            pos = True
    if pos:
        ans = mid
        right = mid-1
    else:
        left = mid+1
print(ans)