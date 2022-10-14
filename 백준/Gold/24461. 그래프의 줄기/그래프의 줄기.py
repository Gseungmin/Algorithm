import sys
input = sys.stdin.readline
N = int(input())
ind = [0]*(N)
tree = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    ind[a] += 1
    ind[b] += 1
from collections import deque
queue = deque()
true = [False]*N
for i in range(N):
    if ind[i] == 1:
        queue.append(i)
        true[i] = True
        
L = len(queue)
ans = []
while 1:
    if L <= 2:
        for i in range(N):
            if true[i] == False:
                ans.append(i)
        for i in queue:
            ans.append(i)
        break
    for i in range(L):
        x = queue.popleft()
        for nx in tree[x]:
            if true[nx] == False:
                ind[nx] -= 1
                if ind[nx] == 1:
                    true[nx] = True
                    queue.append(nx)
    L = len(queue)
ans.sort()
print(" ".join(map(str,ans)))