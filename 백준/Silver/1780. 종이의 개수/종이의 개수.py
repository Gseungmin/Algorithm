import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
ans = [0,0,0]

def RC(N, x1, y1):
    if N == 1:
        ans[graph[x1][y1]+1] += 1
        return
    k = graph[x1][y1]
    check = 0
    for i in range(x1,x1+N):
        for j in range(y1,y1+N):
            if k != graph[i][j]:
                check = 1
                break 
        if check == 1:
            break
    if check == 1:
        RC(N//3, x1, y1)
        RC(N//3, x1+N//3, y1)
        RC(N//3, x1+(N//3)*2, y1)
        RC(N//3, x1, y1+N//3)
        RC(N//3, x1+N//3, y1+N//3)
        RC(N//3, x1+(N//3)*2, y1+N//3)
        RC(N//3, x1, y1+(N//3)*2)
        RC(N//3, x1+N//3, y1+(N//3)*2)
        RC(N//3, x1+(N//3)*2, y1+(N//3)*2)
    else:
        ans[k+1] += 1
    return

RC(N,0,0)
for i in ans:
    print(i)