import sys
input = sys.stdin.readline
N, M = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]
M, K = map(int,input().split())
B = [list(map(int,input().split())) for i in range(M)]
C = [[0]*K for i in range(N)]

def matrix(A, B, C, N, M, K):
    for i in range(N):
        for j in range(M):
            for k in range(K):
                C[i][k] += A[i][j]*B[j][k]
    for i in range(N):
        for j in range(K):
            print(C[i][j], end = " ")
        print()
    return
matrix(A, B, C, N, M, K)