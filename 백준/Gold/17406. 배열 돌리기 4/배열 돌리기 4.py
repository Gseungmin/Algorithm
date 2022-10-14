import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]
B = [[] for i in range(N)]
for i in range(N):
    for j in range(M):
        B[i].append(A[i][j])

m = []
for i in range(K):
    m.append(list(map(int,input().split())))

import itertools
spin = list(itertools.permutations(m))

ans = []
for i in spin:
    B = [[] for x in range(N)]
    for x in range(N):
        for y in range(M):
            B[x].append(A[x][y])
    for j in i:
        r, c, s = j[0]-1, j[1]-1, j[2]
        C = [[] for i in range(N)]
        for x in range(N):
            for y in range(M):
                C[x].append(B[x][y])
        while s>0:
            for a in range(c-s+1, c+s+1):
                B[r-s][a] = C[r-s][a-1]
            for b in range(r-s+1, r+s+1):
                B[b][c+s] = C[b-1][c+s]
            for a in range(c+s-1,c-s-1,-1):
                B[r+s][a] = C[r+s][a+1]
            for b in range(r+s-1,r-s-1,-1):
                B[b][c-s] = C[b+1][c-s]
            s-=1
    Min = -1
    for t in B:
        if Min == -1:
            Min = sum(t)
        else:
            Min = min(sum(t), Min)
    ans.append(Min)
print(min(ans))