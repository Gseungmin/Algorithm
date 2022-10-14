import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = list(map(int,input().split()))
left = 0
right = max(arr)
while left <= right:
    mid = (left+right)//2
    cnt = 0
    i = 0
    k = []
    for j in range(N):
        k.append(arr[j])
        value = max(k)-min(k)
        if value <= mid:
            continue
        else:
            cnt += 1
            i = j
            k = [arr[i]]
            if j == N-1:
                cnt += 1
                k = []
    if k:
        cnt += 1
    if cnt <= M:
        ans = mid
        right = mid-1
    else:
        left = mid+1
print(ans)