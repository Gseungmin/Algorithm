import sys
input = sys.stdin.readline
N, K = map(int,input().split())
if N == K:
    print(0)
    sys.exit()
from collections import deque
queue1 = deque()
queue1.append(K)
true1 = [-1]*(500001)
true1[K] = 0
num = 1
while queue1:
    x = queue1.popleft()
    if x+num <= 500000 and true1[x+num] == -1:
        true1[x+num] = true1[x] + 1
        queue1.append(x+num)
    num += 1
ans = int(1e9)
queue2 = deque()
queue2.append([N,0])
true2 = [[-1]*2 for i in range(500001)]
true2[N][0] = 0
while queue2:
    x, k = queue2.popleft()
    if true1[x] != -1:
        if true2[x][k] == true1[x]:
            ans = min(ans, true1[x])
        if true2[x][k] < true1[x]:
            if k%2 == 0 and true1[x]%2 == 0:
                ans = min(ans, true1[x])
            if k%2 == 1 and true1[x]%2 == 1:
                ans = min(ans, true1[x])
    if x+1 <= 500000 and true2[x+1][1-k] == -1:
        true2[x+1][1-k] = true2[x][k]+1
        queue2.append([x+1,1-k])
    if x-1 >= 0 and true2[x-1][1-k] == -1:
        true2[x-1][1-k] = true2[x][k]+1
        queue2.append([x-1,1-k])
    if x*2 <= 500000 and true2[x*2][1-k] == -1:
        true2[x*2][1-k] = true2[x][k]+1
        queue2.append([x*2,1-k])
if ans == int(1e9):
    print(-1)
else:
    print(ans)