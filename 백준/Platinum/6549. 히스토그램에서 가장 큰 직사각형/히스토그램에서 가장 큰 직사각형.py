import sys
input = sys.stdin.readline
while 1:
    arr = list(map(int,input().split()))
    N, arr = arr[0], arr[1:]
    if N == 0:
        break
    stack = []
    ans = 0
    for i in range(N):
        while stack and arr[stack[-1]] > arr[i]:
            width = i
            height = arr[stack[-1]]
            stack.pop()
            if stack:
                width = i - stack[-1]-1
            ans = max(ans, height*width)
        stack.append(i)
    while stack:
        height = arr[stack.pop()]
        width = N
        if stack:
            width = N - stack[-1] -1
        ans = max(ans, width*height)
    print(ans)