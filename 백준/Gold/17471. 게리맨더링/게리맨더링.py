import sys
input = sys.stdin.readline
N = int(input())
people = [0] + list(map(int,input().split()))
graph = [[] for i in range(N+1)]
for i in range(1,N+1):
    List = list(map(int,input().split()))
    k = List[0]
    for j in range(1,k+1):
        graph[i].append(List[j])

from collections import deque
arr = [i for i in range(1,N+1)]
ans = int(1e9)
for i in range(1,1<<N):
    set1 = set()
    Sum1 = 0
    set2 = set()
    Sum2 = 0
    for j in range(N):
        if i&(1<<j) > 0:
            set1.add(arr[j])
            Sum1 += people[arr[j]]
            k = j
        else:
            set2.add(arr[j])
            Sum2 += people[arr[j]]
            l = j
    if len(set1) == 0 or len(set1) == len(arr):
        continue
    queue = deque()
    queue.append(arr[k])
    true = set()
    true.add(arr[k])
    cnt = 0
    while queue:
        x = queue.popleft()
        cnt += 1
        for nx in graph[x]:
            if nx not in true and nx in set1:
                queue.append(nx)
                true.add(nx)
    queue = deque()
    queue.append(arr[l])
    true = set()
    true.add(arr[l])
    cnt2 = 0
    while queue:
        x = queue.popleft()
        cnt2 += 1
        for nx in graph[x]:
            if nx not in true and nx in set2:
                queue.append(nx)
                true.add(nx)
    if cnt + cnt2 < N:
        continue
    ans = min(ans, abs(Sum2-Sum1))
if ans == int(1e9):
    print(-1)
else:
    print(ans)