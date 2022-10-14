import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
ans = N
sum_room = [list(map(int,input().split())) for i in range(M)]
sum_room.sort()
stack = []
for i, j in sum_room:
    if len(stack) == 0:
        stack.append([i,j])
    else:
        if stack[-1][1] < i:
            stack.append([i,j])
        elif stack[-1][1] == i:
            stack[-1][1] = j
        elif stack[-1][1] > i:
            if stack[-1][1] < j:
                stack[-1][1] = j
for i, j in stack:
    ans -= (j-i)
print(ans)