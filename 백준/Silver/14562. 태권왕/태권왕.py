import sys
input = sys.stdin.readline
C = int(input())
def DFS(s, e, cnt):
    if s > e:
        return
    if s == e:
        ans[cnt] = 1
        return
    DFS(s+s,e+3,cnt+1)
    DFS(s+1,e,cnt+1)
    return
    
for i in range(C):
    S, T = map(int,input().split())
    ans = dict()
    DFS(S, T, 0)
    print(min(ans.keys()))