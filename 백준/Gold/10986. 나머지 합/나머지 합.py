import sys
input = sys.stdin.readline
N, M = map(int,input().split())
Sum = [0]*(N+1)
List = list(map(int,input().split()))
value = 0
for i in range(N):
    value += List[i]
    Sum[i+1] = value
cnt = dict()
cnt[0] = 1
ans = 0
for i in range(1,N+1):
    if Sum[i]%M in cnt:
        ans += cnt[Sum[i]%M]
    if Sum[i]%M in cnt:
        cnt[Sum[i]%M] += 1
    else:
        cnt[Sum[i]%M] = 1
print(ans)