import sys
input = sys.stdin.readline
N = int(input())
List = list(map(int,input().split()))
graph = [[] for i in range(N)]
for i in range(N-1):
    for j in range(i+1,N):
        if List[i] < List[j]:
            graph[i].append(j)
ans = [0]
def DFS(index, cnt):
    check = 0
    for i in graph[index]:
        check = 1
        if dp[i] != -1:
            ans[0] = max(ans[0], cnt+dp[i]+1)
        else:
            DFS(i, cnt+1)
    if check == 0:
        ans[0] = max(ans[0], cnt)
    return

dp = [-1]*N
for i in range(N-1,-1,-1):
    if dp[i] == -1:
        ans = [0]
        DFS(i, 0)
        dp[i] = ans[0]
print(max(dp)+1)