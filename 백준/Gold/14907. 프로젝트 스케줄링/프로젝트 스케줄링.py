ind = dict()
graph = dict()
time = dict()
while 1:
    try:
        List = list(map(str,input().split()))
    except:
        break
    if len(List) == 2:
        a, b = List[0], List[1]
        ind[a] = 0
        time[a] = int(b)
    else:
        a, b, c = List[0], List[1], List[2]
        ind[a] = len(c)
        time[a] = int(b)
        for i in c:
            if i not in graph:
                graph[i] = []
            graph[i].append(a)
import heapq
heap = []
true = set()
for i in ind:
    if ind[i] == 0:
        heapq.heappush(heap,[time[i],i])
        true.add(i)
ans = 0
while heap:
    t, x = heapq.heappop(heap)
    ans += t
    for i in heap:
        i[0] -= t
    if x not in graph:
        continue
    for nx in graph[x]:
        if nx not in true:
            ind[nx] -= 1
            if ind[nx] == 0:
                heapq.heappush(heap,[time[nx], nx])
                true.add(nx)
print(ans)