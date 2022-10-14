import sys
input = sys.stdin.readline
N = int(input())
jump = [list(map(int,input().split())) for i in range(N-1)]
K = int(input())

INF = int(1e9)
ans = [INF]
def RC(index, cnt, energy):
    if index >= N:
        return
    if index == N-1:
        ans[0] = min(ans[0], energy)
        return
    if cnt == 0:
        RC(index+1, cnt, energy+jump[index][0])
        RC(index+2, cnt, energy+jump[index][1])
        RC(index+3, cnt+1, energy+K)
    else:
        RC(index+1, cnt, energy+jump[index][0])
        RC(index+2, cnt, energy+jump[index][1])
    return
RC(0, 0, 0)
print(ans[0])