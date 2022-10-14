import sys
input = sys.stdin.readline
N, M = map(int,input().split())
List = list(map(int,input().split()))
if N == 1:
    print(List[0])
    sys.eixt()
left = 1
right = sum(List)
ans = 0
while left <= right:
    mid = (left+right)//2
    cnt = 0
    Sum = 0
    check = 0
    for i in range(N):
        Sum += List[i]
        if Sum > mid:
            cnt += 1
            Sum = List[i]
            if Sum > mid:
                check = -1
                break
        elif Sum == mid:
            cnt += 1
            if i != N-1:
                Sum = 0
    if Sum < mid:
        cnt += 1
    if check == -1:
        left = mid + 1
        continue
    if cnt <= M:
        ans = mid
        right = mid-1
    else:
        left = mid+1
print(ans)