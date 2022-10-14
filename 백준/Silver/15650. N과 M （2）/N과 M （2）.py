import sys
input = sys.stdin.readline
N, M = map(int,input().split())
ans = []
def N_and_M(N, M, start, ans):
    if M == 0:
        for i in range(len(ans)):
            if i == len(ans)-1:
                print(ans[i])
            else:
                print(ans[i], end = " ")
        return
    for index in range(start, N+1):
        ans.append(index)
        N_and_M(N, M-1, index + 1, ans)
        ans.pop(-1)
    return
N_and_M(N, M, 1, ans)