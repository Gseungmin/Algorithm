import sys
input = sys.stdin.readline
N = int(input())
List = list(map(int,input().split()))
down = []
up = []
for i in List:
    if i < 0:
        down.append([-i,-1])
    else:
        up.append([i,1])
up.sort()
down.sort()

if not down:
    print(up[0][0], up[1][0])
    sys.exit()
if not up:
    print(-down[1][0],-down[0][0])
    sys.exit()

ans = int(1e9)
left = 0
right = 0
if len(up) >= 2:
    ans = up[0][0]+up[1][0]
    left = up[0][0]
    right = up[1][0]
if len(down) >= 2:
    if ans > abs(-down[0][0]-down[1][0]):
        ans = abs(-down[0][0]-down[1][0])
        left = -down[0][0]
        right = -down[1][0]

List = up+down
List.sort()
for i in range(1,N):
    if List[i-1][1] != List[i][1]:
        if List[i-1][1] == -1:
            if ans > abs(-List[i-1][0]+List[i][0]):
                left = -List[i-1][0]
                right = List[i][0]
                ans = min(ans, abs(-List[i-1][0]+List[i][0]))
        if List[i-1][1] == 1:
            if ans > abs(List[i-1][0]-List[i][0]):
                left = List[i-1][0]
                right = -List[i][0]
                ans = min(ans, abs(List[i-1][0]-List[i][0]))
print(min(left, right), max(left, right))
