import sys
input = sys.stdin.readline
N = int(input())

weight = []
height = [0]*(N)
size = []

info = []

for i in range(N):
    a, b, c = map(int,input().split())
    info.append([i,a,b,c])
    size.append([a,i])
    weight.append([c,i])
    height[i] = b

size.sort(reverse = True)
weight.sort(reverse = True)

import copy

bigger_size = dict()
for i in range(len(size)):
    if i == 0:
        bigger_size[size[i][1]] = set()
    else:
        bigger_size[size[i][1]] = copy.deepcopy(bigger_size[size[i-1][1]])
        bigger_size[size[i][1]].add(size[i-1][1])
        
bigger_weight = dict()
for i in range(len(weight)):
    if i == 0:
        bigger_weight[weight[i][1]] = set()
    else:
        bigger_weight[weight[i][1]] = copy.deepcopy(bigger_weight[weight[i-1][1]])
        bigger_weight[weight[i][1]].add(weight[i-1][1])
        
dp = [[0]*N for i in range(N)]
last = [0,0]
prev = [[-1]*N for i in range(N)]

ans = 0
for i in range(N):
    dp[0][i] = height[i]
    if ans < height[i]:
        ans = height[i]
        last = [0,i]

if dp[0][size[0][1]] > dp[0][weight[0][1]]:
    last = [0,size[0][1]]
else:
    last = [0,weight[0][1]]

for i in range(N-1):
    for j in range(N):
        if dp[i][j] != 0: 
            for k in range(N): #k가 다음 무게가 더 가볍고 넓이가 더 좁다면
                if j in bigger_size[k] and j in bigger_weight[k]:
                    if dp[i+1][k] < dp[i][j] + height[k]:
                        dp[i+1][k] = dp[i][j] + height[k]
                        prev[i+1][k] = j
                    if dp[i+1][k] > ans:
                        ans = dp[i+1][k]
                        last = [i+1,k]

ans = []
h, i = last[0], last[1]

while h != -1:
    ans.append([h,i]) #층 높이, 블록 인덱스
    i, h = prev[h][i], h-1

print(len(ans))
for i in ans:
    print(i[1]+1)