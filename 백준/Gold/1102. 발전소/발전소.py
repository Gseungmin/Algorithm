import sys
input = sys.stdin.readline
N = int(input())
cost = [list(map(int,input().split())) for i in range(N)]
List = list(input().strip())
P = int(input())
k = 0
cnt = 0
for i in range(len(List)):
    if List[i] == "Y":
        k = k|(1<<i)
        cnt += 1
if cnt >= P:
    print(0)
    sys.exit()
if cnt == 0:
    if P == 0:
        print(0)
    else:
        print(-1)
    sys.exit()
INF = 1000
dp = [INF]*(1<<N)
dp[k] = 0
from collections import deque
queue = deque()
queue.append([k,0])
Min = INF
while cnt < P:
    size = len(queue)
    for s in range(size):
        bit, k = queue.popleft()
        for i in range(N):
            if bit&(1<<i) == 0:
                tmp = 1000
                for j in range(N):
                    if i == j:
                        continue
                    if (1<<j) & bit != 0:
                        tmp = min(tmp, cost[j][i])
                nc = bit|(1<<i)
                if dp[nc] > k+tmp:
                    queue.append([nc,k+tmp])
                    dp[nc] = k+tmp
    cnt += 1
while queue:
    x, y = queue.popleft()
    Min = min(Min,y)
print(Min)