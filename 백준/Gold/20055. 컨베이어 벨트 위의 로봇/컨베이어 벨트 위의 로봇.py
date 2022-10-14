import sys
input = sys.stdin.readline
N, L = map(int,input().split())
A = list(map(int,input().split()))
Dict = dict()
Robot = dict()
for i in range(1,2*N+1):
    Dict[i] = A[i-1]
    Robot[i] = False
cnt = 0
ans = 0
while cnt < L:
    ans += 1
    K = dict()
    M = dict()
    for i in range(1,2*N+1):
        if i == 2*N:
            K[1] = Dict[2*N]
            M[1] = Robot[2*N]
        else:
            K[i+1] = Dict[i]
            M[i+1] = Robot[i]
    if M[N] == True:
        M[N] = False
    for i in range(N-1,1,-1):
        if M[i] == True:
            if M[i+1] == False and K[i+1] >= 1:
                M[i+1] = True
                K[i+1] -= 1
                M[i] = False
                if K[i+1] == 0:
                    cnt += 1
    if M[N] == True:
        M[N] = False
    if M[1] == False and K[1] >= 1:
        M[1] = True
        K[1] -= 1
        if K[1] == 0:
            cnt += 1
    Robot = M.copy()
    Dict = K.copy()
print(ans)