import sys
input = sys.stdin.readline
N = int(input())
ans = 0
stack = []

for i in range(N):
    h = int(input())
    while stack and stack[-1][0] < h:
        ans += stack.pop()[1]
    
    if stack and stack[-1][0] == h:
        cnt = stack.pop()[1]
        ans += cnt
        if stack:
            ans += 1
        stack.append((h,cnt+1))
    else:
        if len(stack) != 0:
            ans += 1
        stack.append((h,1))
print(ans)