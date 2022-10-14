import sys
input = sys.stdin.readline
N, M = map(int,input().split())
Dict = dict()
for i in range(M):
    Dict[i] = list(map(int,input().split()))[1:]

ans = 1000
for i in range(1,1<<M):
    cnt = 0
    List = set()
    for j in range(M):
        if i&(1<<j) > 0:
            cnt += 1
            for k in Dict[j]:
                List.add(k)
    if len(List) == N:
        ans = min(ans, cnt)
if ans == 1000:
    print(-1)
else:
    print(ans)