import sys
input = sys.stdin.readline
N, S = map(int,input().split())
List = list(map(int,input().split()))
ans = 0
for i in range(1,1<<N):
    Sum = 0
    for k in range(N):
        if i&(1<<k) > 0:
            Sum += List[k]
    if Sum == S:
        ans += 1
print(ans)