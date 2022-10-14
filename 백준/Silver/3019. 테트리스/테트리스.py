import sys
input = sys.stdin.readline
C, P = map(int,input().split())
graph = list(map(int,input().split()))

if P == 1:
    ans = C
    for i in range(3, C):
        if graph[i] == graph[i-1] == graph[i-2] == graph[i-3]:
            ans += 1
    print(ans)
elif P == 2:
    ans = 0
    for i in range(1, C):
        if graph[i] == graph[i-1]:
            ans += 1
    print(ans)
elif P == 3:
    ans = 0
    for i in range(2, C):
        if graph[i]-1 == graph[i-1] == graph[i-2]:
            ans += 1
    for i in range(1, C):
        if graph[i-1] == graph[i]+1:
            ans += 1
    print(ans)
elif P == 4:
    ans = 0
    for i in range(2, C):
        if graph[i] == graph[i-1] == graph[i-2]-1:
            ans += 1
    for i in range(1, C):
        if graph[i] == graph[i-1]+1:
            ans += 1
    print(ans)
elif P == 5:
    ans = 0
    for i in range(1, C):
        if graph[i] == graph[i-1]+1:
            ans += 1
    for i in range(1, C):
        if graph[i-1] == graph[i]+1:
            ans += 1
    for i in range(2, C):
        if graph[i] == graph[i-1] == graph[i-2]:
            ans += 1
    for i in range(2, C):
        if graph[i] == graph[i-1]+1 == graph[i-2]:
            ans += 1
    print(ans)
elif P == 6:
    ans = 0
    for i in range(2, C):
        if graph[i] == graph[i-1] == graph[i-2]:
            ans += 1
    for i in range(1, C):
        if graph[i] == graph[i-1]:
            ans += 1
    for i in range(2, C):
        if graph[i] == graph[i-1] == graph[i-2]+1:
            ans += 1
    for i in range(1, C):
        if graph[i]+2 == graph[i-1]:
            ans += 1
    print(ans)
elif P == 7:
    ans = 0
    for i in range(2, C):
        if graph[i] == graph[i-1] == graph[i-2]:
            ans += 1
    for i in range(1, C):
        if graph[i] == graph[i-1]:
            ans += 1
    for i in range(2, C):
        if graph[i]+1 == graph[i-1] == graph[i-2]:
            ans += 1
    for i in range(1, C):
        if graph[i] == graph[i-1]+2:
            ans += 1
    print(ans)