import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N, M = map(int,input().split())
List = [0] + list(map(int,input().split()))

def RC(index, size, K):
    if K == M:
        ans[0] = max(ans[0], size)
        return
    if index+1 <= N:
        RC(index+1, size+List[index+1], K+1)
    else:
        ans[0] = max(ans[0], size)
    if index+2 <= N:
        RC(index+2, size//2+List[index+2], K+1)
    else:
        ans[0] = max(ans[0], size)
    return

ans = [0]
RC(0,1,0)
print(ans[0])