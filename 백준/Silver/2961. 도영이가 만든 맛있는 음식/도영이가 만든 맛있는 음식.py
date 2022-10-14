import sys
input = sys.stdin.readline
N = int(input())
List = [list(map(int,input().split())) for i in range(N)]

INF = int(1e9)
arr = []
ans = [INF]
def RC(index):
    if index == N:
        if len(arr) > 0:
            S = 1
            B = 0
            for i in arr:
                S *= i[0]
                B += i[1]
            ans[0] = min(ans[0], abs(S-B))
        return
    arr.append(List[index])
    RC(index+1)
    arr.pop()
    RC(index+1)
    return
RC(0)
print(ans[0])