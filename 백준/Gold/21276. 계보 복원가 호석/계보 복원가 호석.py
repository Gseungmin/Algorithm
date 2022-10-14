N = int(input())
parent = dict()
ind = dict()
true = dict()
ans = dict()
List = list(input().split())
for i in List:
    ind[i] = 0
    parent[i] = []
    true[i] = False
    ans[i] = []
M = int(input())
for i in range(M):
    a, b = map(str,input().split())
    parent[b].append(a)
    ind[a] += 1

from collections import deque
arr = []
for i in ind:
    if ind[i] == 0:
        arr.append(i)
        true[i] = True
arr.sort()
print(len(arr))
print(" ".join(arr))
arr = deque(arr)
while arr:
    x = arr.popleft()
    for nx in parent[x]:
        if true[nx] == False:
            ind[nx] -= 1
            if ind[nx] == 0:
                true[nx] = True
                arr.append(nx)
                ans[x].append(nx)
key = list(ans.keys())
key.sort()
for i in key:
    ans[i].sort()
    if len(ans[i]) == 0:
        print(i, len(ans[i]))
    else:
        print(i, len(ans[i]), " ".join(ans[i]))