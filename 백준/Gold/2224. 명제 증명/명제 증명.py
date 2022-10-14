N = int(input())
List = set()
Dict = dict()
for i in range(N):
    arr = list(map(str,input().split()))
    for i in arr:
        if i != "=>":
            List.add(i)
    if arr[0] == arr[-1]:
        continue
    Dict[(arr[0],arr[-1])] = 1
List = list(List)
List.sort()
M = len(List)
INF = int(1e9)
dist = [[INF]*M for i in range(M)]
for i in range(M):
    for j in range(M):
        if (List[i], List[j]) in Dict:  
            dist[i][j] = 1
for k in range(M):
    for i in range(M):
        if i == k:
            continue
        for j in range(M):
            if i == j or k == j:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
ans = []
for i in range(M):
    for j in range(M):
        if dist[i][j] != INF:
            ans.append(List[i]+" => "+List[j]) 
print(len(ans))
for i in ans:
    print(i)