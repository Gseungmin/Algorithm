import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
d = [[[-1]*21 for j in range(2)] for i in range(N-2)]
if 0 <= arr[0]+arr[1] <= 20:
    d[0][0][arr[0]+arr[1]] = 1
if 0 <= arr[0]-arr[1] <= 20:
    d[0][1][arr[0]-arr[1]] = 1
for i in range(1,N-2):
    for j in range(2):
        for k in range(21):
            if j == 0:
                if k-arr[i+1] >= 0:
                    if d[i-1][0][k-arr[i+1]] != -1:
                        if d[i][0][k] == -1:
                            d[i][0][k] = d[i-1][0][k-arr[i+1]]
                        else:
                            d[i][0][k] += d[i-1][0][k-arr[i+1]]
                    if d[i-1][1][k-arr[i+1]] != -1:
                        if d[i][0][k] == -1:
                            d[i][0][k] = d[i-1][1][k-arr[i+1]]
                        else:
                            d[i][0][k] += d[i-1][1][k-arr[i+1]]
            if j == 1:
                if k+arr[i+1] <= 20:
                    if d[i-1][0][k+arr[i+1]] != -1:
                        if d[i][1][k] == -1:
                            d[i][1][k] = d[i-1][0][k+arr[i+1]]
                        else:
                            d[i][1][k] += d[i-1][0][k+arr[i+1]]
                    if d[i-1][1][k+arr[i+1]] != -1:
                        if d[i][1][k] == -1:
                            d[i][1][k] = d[i-1][1][k+arr[i+1]]
                        else:
                            d[i][1][k] += d[i-1][1][k+arr[i+1]]
if d[-1][0][arr[-1]] != -1 and d[-1][1][arr[-1]] != -1:
    print(d[-1][0][arr[-1]]+d[-1][1][arr[-1]])
elif d[-1][0][arr[-1]] == -1 and d[-1][1][arr[-1]] != -1:
    print(d[-1][1][arr[-1]])
elif d[-1][0][arr[-1]] != -1 and d[-1][1][arr[-1]] == -1:
    print(d[-1][0][arr[-1]])
elif d[-1][0][arr[-1]] == -1 and d[-1][1][arr[-1]] == -1:
    print(0)