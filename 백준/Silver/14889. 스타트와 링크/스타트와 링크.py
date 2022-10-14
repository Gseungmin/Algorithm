import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]

ans = int(1e9)
for i in range(1,1<<N):
    List1 = []
    List2 = []
    for k in range(N):
        if i & (1<<k) > 0:
            List1.append(k)
        else:
            List2.append(k)
    if len(List1) != len(List2):
        continue
    Sum1 = 0
    Sum2 = 0
    for a in range(len(List1)-1):
        for b in range(a+1, len(List1)):
            Sum1 += (graph[List1[a]][List1[b]]+graph[List1[b]][List1[a]])
            Sum2 += (graph[List2[a]][List2[b]]+graph[List2[b]][List2[a]])
    ans = min(ans,abs(Sum2-Sum1))
print(ans)