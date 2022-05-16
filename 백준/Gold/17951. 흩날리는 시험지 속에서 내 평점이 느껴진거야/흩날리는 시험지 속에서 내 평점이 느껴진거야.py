import sys
input = sys.stdin.readline
N, K = map(int,input().split())
List = list(map(int,input().split()))
Sum = [0]*N
s = 0
for i in range(N):
    s += List[i]
    Sum[i] = s
INF = int(1e9)
left = 0
right = INF
ans = []
while left <= right:
    mid = (left+right)//2
    pos = False
    cnt = 0
    i = 0
    j = 0
    while j < N:
        if i == 0:
            value = Sum[j]
        else:
            value = Sum[j]-Sum[i-1]
        if value < mid:
            j += 1
        elif value == mid:
            pos = True
            i = j+1
            j = i
            cnt += 1
        else:
            i = j+1
            j = i
            cnt += 1
    if cnt >= K:
        left = mid+1
        ans = mid
    elif cnt < K:
        right = mid-1
print(ans)