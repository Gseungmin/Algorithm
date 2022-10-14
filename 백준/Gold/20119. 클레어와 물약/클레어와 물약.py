import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
ind = dict()
for i in range(M):
    List = list(map(int,input().split()))
    for j in range(1,len(List)-1):
        graph[List[j]].append(List[-1])
    if List[-1] not in ind:
        ind[List[-1]] = []
    ind[List[-1]].append([List[0]])
    ind[List[-1]][-1].append(set(List[1:-1]))
    
K = int(input())
from collections import deque
queue = deque(list(map(int,input().split())))
true = [False]*(N+1)
cnt = 0
for i in queue:
    cnt += 1
    true[i] = True
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if true[nx] == False:
            for k in ind[nx]:
                if x in k[1]:
                    k[0] -= 1
                if k[0] == 0:
                    cnt += 1
                    true[nx] = True
                    queue.append(nx)
print(cnt)
for i in range(1,N+1):
    if true[i] == True:
        print(i, end = " ")