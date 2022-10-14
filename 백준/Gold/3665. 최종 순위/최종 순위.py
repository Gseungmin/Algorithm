import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
    N = int(input())
    ind = [0]*(N+1)
    graph = [set() for i in range(N+1)]
    List = list(map(int,input().split()))
    for i in range(len(List)-1):
        for j in range(i+1,len(List)):
            graph[List[i]].add(List[j])
    for i in range(len(List)):
        ind[List[i]] = i
    m = int(input())
    for i in range(m):
        a, b = map(int,input().split())
        if b in graph[a]:
            graph[a].discard(b)
            graph[b].add(a)
            ind[b] -= 1
            ind[a] += 1
        elif a in graph[b]:
            graph[b].discard(a)
            graph[a].add(b)
            ind[b] += 1
            ind[a] -= 1
    ans = []
    queue = deque()
    true = [False]*(N+1)
    for i in range(1,N+1):
        if ind[i] == 0:
            queue.append(i)
            true[i] = True
    if len(queue) >= 2:
        print("?")
        continue
    check = 0
    while queue:
        x = queue.popleft()
        ans.append(x)
        cnt = 0
        for nx in graph[x]:
            if true[nx] == False:
                ind[nx] -= 1
                if ind[nx] == 0:
                    cnt += 1
                    queue.append(nx)
                    true[nx] = True
            if cnt >= 2:
                check = 1
                break
        if check == 1:
            break
    if check == 1:
        print("?")
        continue
    if len(ans) != N:
        print("IMPOSSIBLE")
    else:
        print(" ".join(map(str,ans)))