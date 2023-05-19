import sys
input = sys.stdin.readline

N, M = map(int,input().split())

student = [0]*(N+1)
info = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    info[a].append(b)
    student[b] += 1

from collections import deque
true = [False]*(N+1)
queue = deque()
for i in range(1,N+1):
    if student[i] == 0:
        queue.append(i)
        true[i] = True

ans = []
while queue:
    x = queue.popleft()
    ans.append(x)
    for nx in info[x]:
        if true[nx] == False:
            student[nx] -= 1
            if student[nx] == 0:
                true[nx] = True
                queue.append(nx)
print(" ".join(map(str,ans)))