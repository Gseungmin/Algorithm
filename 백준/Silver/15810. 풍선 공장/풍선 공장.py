import sys
input = sys.stdin.readline
N, M = map(int,input().split())
List = list(map(int,input().split()))
left = 1
right = max(List)*M
ans = right
while left<= right:
    mid = (left+right)//2
    K = 0
    for i in List:
        K += mid//i
    if K >= M:
        ans = mid
        right = mid-1
    elif K < M:
        left = mid+1
print(ans)