import sys
input = sys.stdin.readline
t = int(input())
N = int(input())
left = list(map(int,input().split()))
M = int(input())
right = list(map(int,input().split()))
Dict = dict()
for i in range(N):
    k = left[i]
    if k not in Dict:
        Dict[k] = 1
    else:
        Dict[k] += 1
    for j in range(i+1,N):
        k += left[j]
        if k not in Dict:
            Dict[k] = 1
        else:
            Dict[k] += 1
    k -= left[i]
ans = 0
for i in range(M):
    k = right[i]
    if t-k in Dict:
        ans += Dict[t-k]
    for j in range(i+1,M):
        k += right[j]
        if t-k in Dict:
            ans += Dict[t-k]
    k -= right[i]
print(ans)