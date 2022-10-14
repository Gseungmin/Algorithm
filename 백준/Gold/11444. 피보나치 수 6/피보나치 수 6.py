import sys
input = sys.stdin.readline
M = int(input())
A = [[1,1],[1,0]]

def RC(A, M):
    if M == 0:
        return [[1,1],[1,1]]
    if M == 1:
        for i in range(2):
            for j in range(2):
                A[i][j] %= 1000
        return A
    if M % 2 == 0:
        temp = RC(A, M//2)
        return mul(temp, temp, 2)
    if M % 2 == 1:
        return mul(RC(A, M-1), A, 2)

def mul(A, B, N):
    C = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += (A[i][k]*B[k][j]) % 1000000007
            C[i][j] %= 1000000007
    return C
ans = RC(A, M)
print(ans[0][1]%1000000007)