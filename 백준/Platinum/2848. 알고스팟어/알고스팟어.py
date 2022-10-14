N = int(input())
graph = dict()
ind = dict()
true = dict()
List = [input() for i in range(N)]
for i in List:
    for j in i:
        if j not in graph:
            graph[j] = set()
        if j not in ind:
            ind[j] = 0
            true[j] = False

for i in range(N-1):
    for j in range(i+1,N):
        a = List[i]
        b = List[j]
        index = min(len(a), len(b))
        check = 0
        for k in range(index):
            x, y = a[k], b[k]
            if x != y:
                check = 1
                if y not in graph[x]:
                    graph[x].add(y)
                    ind[y] += 1
                break
        if check == 0 and len(a) > len(b):
            print("!")
            exit()

from collections import deque
queue = deque()
for i in ind:
    if ind[i] == 0:
        queue.append([i,i])
        true[i] = True
if not queue:
    print("!")
    exit()

ans = []
while queue:
    k, x = queue.popleft()
    if len(k) == len(graph):
        ans.append(k)
    for nx in graph[x]:
        if true[nx] == False:
            ind[nx] -= 1
            if ind[nx] == 0:
                true[nx] = True
                queue.append([k+nx,nx])
for i in true:
    if true[i] == False:
        print("!")
        exit()

if len(ans) == 1:
    print(ans[0])
else:
    print("?")