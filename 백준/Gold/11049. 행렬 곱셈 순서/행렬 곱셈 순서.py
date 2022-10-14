import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
memo = [[0]*N for i in range(N)]

for i in range(2, len(arr)+1):
    for j in range(len(arr)):
        if i == 2:
            if j == len(arr)-1:
                break
            memo[j][j+1] = arr[j][0]*arr[j][1]*arr[j+1][1]
            continue
        if j+i-1 < len(arr):
            k = j
            while k < j+i-1:
                if k == j:
                    memo[j][j+i-1] = arr[j][0]*arr[k][1]*arr[j+i-1][1]+memo[k+1][j+i-1]
                elif k == j+i-2:
                    memo[j][j+i-1] = min(memo[j][j+i-1], memo[j][k]+arr[j][0]*arr[k][1]*arr[j+i-1][1])
                else:
                    memo[j][j+i-1] = min(memo[j][j+i-1], memo[j][k]+memo[k+1][j+i-1]+arr[j][0]*arr[k][1]*arr[j+i-1][1])
                k += 1
print(memo[0][N-1])