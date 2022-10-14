import sys
input = sys.stdin.readline
N, K = map(int,input().split())
arr = [int(input()) for i in range(N)]
arr.sort()
total = 0
for i in range(N-1,-1,-1):
    total += K//arr[i]
    K = K - (K//arr[i])*arr[i]
print(total)