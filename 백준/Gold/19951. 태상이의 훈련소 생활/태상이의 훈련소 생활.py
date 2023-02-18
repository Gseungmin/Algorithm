import sys
input = sys.stdin.readline
import heapq
N, M = map(int,input().split())
arr = list(map(int,input().split()))
List = [0]*N
ans = [0]*N

#누적합 초기화
for i in range(M):
    a, b, c = map(int,input().split())
    a, b = a-1, b-1
    List[a] += c
    if b+1 != N:
        List[b+1] -= c

change = 0
for i in range(N):
    change += List[i]
    ans[i] = str(arr[i] + change)

print(" ".join(ans))