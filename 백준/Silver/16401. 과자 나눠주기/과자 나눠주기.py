import sys
input = sys.stdin.readline
M, N = map(int,input().split())
cookies = list(map(int,input().split()))
left = 1
right = max(cookies)
ans = 0

def check(mid):
    cnt = 0
    for i in cookies:
        cnt += i//mid
    if M <= cnt:
        return True
    return False

while left <= right:
    mid = (left+right)//2
    if check(mid):
        ans = mid
        left = mid+1
    else:
        right = mid-1
print(ans)