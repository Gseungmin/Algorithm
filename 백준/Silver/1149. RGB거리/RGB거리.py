import sys
input = sys.stdin.readline
N = int(input())
memo = []
memo.append([0,0,0])
R, G, B = map(int,input().split())
memo.append([R,G,B])
for i in range(2,N+1):
    memo.append([0,0,0])
    R, G, B = map(int,input().split())
    memo[i][0] = min(memo[i-1][1], memo[i-1][2]) + R
    memo[i][1] = min(memo[i-1][0], memo[i-1][2]) + G
    memo[i][2] = min(memo[i-1][0], memo[i-1][1]) + B
print(min(memo[N]))