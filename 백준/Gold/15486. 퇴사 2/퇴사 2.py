import sys
input = sys.stdin.readline
N = int(input())
T = []
P = []
for i in range(N):
    a,b = map(int,input().split())
    T.append(a)
    P.append(b)
D = [0]*(N+1)
for i in range(N):
    if i+T[i] <= N:
        D[i+T[i]] = max(D[i+T[i]], D[i]+P[i])
    D[i+1] = max(D[i+1], D[i])
print(D[-1])