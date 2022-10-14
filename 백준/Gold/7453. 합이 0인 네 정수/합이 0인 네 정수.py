import sys
input = sys.stdin.readline
A = []
B = []
C = []
D = []
N = int(input())
for i in range(N):
    a, b, c, d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = dict()
CD = dict()

for i in range(N):
    for j in range(N):
        k = A[i]+B[j]
        if k not in AB:
            AB[k] = 1
        else:
            AB[k] += 1
ans = 0
for i in range(N):
    for j in range(N):
        k = C[i]+D[j]
        if -k in AB:
            ans += AB[-k]
        
print(ans)