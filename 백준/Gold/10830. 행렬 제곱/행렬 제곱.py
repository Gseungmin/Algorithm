import sys
input = sys.stdin.readline
N, B = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]

def matrix(a, b, N):
    c = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][k] += a[i][j]*b[j][k]
                c[i][k] %= 1000
    return c

def math(A, B, N):
    if B == 1:
        return A
    elif B == 2:
        return matrix(A, A, N)
    elif B % 2 == 0:
        C = math(A, B//2, N)
        return matrix(C, C, N)
    elif B % 2 == 1:
        return matrix(A, math(A, B-1, N), N)

answer = math(A, B, N)
for i in range(N):
    for j in range(N):
        print(answer[i][j]%1000, end = " ")
    print()