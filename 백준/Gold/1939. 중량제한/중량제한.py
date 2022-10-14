import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
left = 1
right = 1
for i in range(M):
    a, b, c = map(int,input().split())
    right = max(right, c)
    graph[a].append([b,c])
    graph[b].append([a,c])
x, y = map(int,input().split())

from collections import deque
while left <= right:
    mid = (left+right)//2   
    queue = deque()
    true = [False]*(N+1)
    check = 0
    true[x] = True
    queue.append(x)
    while queue:
        a = queue.popleft()
        if a == y:
            check = 1
            break
        for b in graph[a]:
            Next = b[0]
            value = b[1]
            if true[Next] == False and value >= mid:
                true[Next] = True
                queue.append(Next)
    if check == 1:
        ans = mid
        left = mid+1
    else:
        right = mid-1
print(ans)