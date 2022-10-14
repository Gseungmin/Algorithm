import sys
input = sys.stdin.readline
N, K, M = map(int,input().split())
a = [[False]*N for i in range(N)]
for i in range(N):
    x, y = map(int,input().split())
    a[i][x-1] = True
    a[i][y-1] = True

def mul(a,b):
    c = [[False]*N for i in range(N)]
    for i in range(N):
        for k in range(N):
            if a[i][k] == False:
                continue
            for j in range(N):
                if a[i][k] and b[k][j]:
                    c[i][j] = True
    return c

def pow(a, m):
    ans = [[False]*N for i in range(N)]
    for i in range(N):
        ans[i][i] = True
    while m>0:
        if m%2==1:
            ans = mul(ans,a)
        a = mul(a,a)
        m //= 2
    return ans

ans = pow(a, K)
for i in range(M):
    a, b = map(int,input().split())
    if ans[a-1][b-1] == False:
        print("life")
    else:
        print("death")