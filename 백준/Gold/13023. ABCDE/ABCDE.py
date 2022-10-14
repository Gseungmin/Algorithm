import sys
input = sys.stdin.readline
N, E = map(int,input().split())
G_1 = [] #인접행렬
G_2 = [] #인접리스트
Edge = [] #간선리스트
for i in range(N):
    G_1.append([0]*N)
    G_2.append([])
for i in range(E):
    A, B = map(int,input().split())
    G_1[A][B] = 1
    G_1[B][A] = 1
    G_2[A].append(B)
    G_2[B].append(A)
    Edge.append([A,B])
    Edge.append([B,A])
E *= 2
for i in range(E):
    for j in range(E):
        A, B = Edge[i]
        C, D = Edge[j]
        if A == B or A == C or A == D or B == C or B == D or C == D: #간접리스트
            continue
        if G_1[B][C] != 1: #인접행렬
            continue
        for k in G_2[D]: #인접리스트
            if k == A or k == B or k == C or k == D:
                continue
            print(1)
            sys.exit(0)
print(0)