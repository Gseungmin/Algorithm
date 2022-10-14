import sys
input = sys.stdin.readline

N, M = map(int,input().split())
s, e = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

from collections import deque
def BFS(x,mid):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for nx, t in graph[x]:
            if t < mid:
                continue
            if nx not in true:
                true.add(nx)
                queue.append(nx)
                if e in true:
                    return True
    return False
    
left = 1
right = 1000000
ans = 0
while left <= right:
    mid = (left+right)//2
    true = set()
    true.add(s)
    BFS(s,mid)
    if e in true:
        left = mid+1
        ans = mid
    else:
        right = mid-1
print(ans)