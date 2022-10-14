import sys
input = sys.stdin.readline
N = int(input())
grape = [[0]]
ans = [[0,0,0]]
for i in range(N):
    grape.append(int(input()))
    ans.append([0,0,0])
ans[1][1] = grape[1]
for i in range(2,N+1):
    ans[i][0] = max(ans[i-1][0], ans[i-1][1], ans[i-1][2])
    ans[i][1] = ans[i-1][0] + grape[i]
    ans[i][2] = ans[i-1][1] + grape[i]
print(max(ans[N]))