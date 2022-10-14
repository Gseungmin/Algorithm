import sys
input = sys.stdin.readline
N, K = map(int,input().split())
arr = list(map(int,input().split()))
left, right = 0, 0
Sum = arr[0]
ans = int(1e9)
while 1:
    if Sum < K:
        right += 1
        if right == N:
            break
        Sum += arr[right]
    elif Sum >= K:
        ans = min(ans,right-left+1)
        Sum -= arr[left]
        left += 1
        if left == N:
            break
        right = max(left, right)
        if right == left:
            Sum = arr[right]
if ans == int(1e9):
    print(0)
else:
    print(ans)