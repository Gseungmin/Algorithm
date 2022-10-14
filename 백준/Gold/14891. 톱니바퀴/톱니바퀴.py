Dict = dict()
for i in range(1,5):
    N = list(input())
    Dict[i] = []
    for j in N:
        Dict[i].append(int(j))
K = int(input())
from collections import deque
for i in range(K):
    N, D = map(int,input().split())
    queue = deque()
    queue.append([N,D])
    true = [False]*(5)
    true[N] = True
    Set = set()
    while queue:
        x, d = queue.popleft()
        Set.add((x,d))
        mx = x-1
        nx = x+1
        if mx > 0:
            if true[mx] == False:
                if Dict[mx][2] != Dict[x][6]:
                    queue.append([mx,-d])
                    true[mx] = True
        if nx <= 4:
            if true[nx] == False:
                if Dict[nx][6] != Dict[x][2]:
                    queue.append([nx,-d])
                    true[nx] = True
    for n, d in Set:
        k = []
        if d == 1:
            k = [Dict[n][7]]
            for i in range(7):
                k.append(Dict[n][i])
            Dict[n] = k.copy()
        if d == -1:
            for i in range(1,8):
                k.append(Dict[n][i])
            k.append(Dict[n][0])
            Dict[n] = k.copy()
ans = 0
for i in range(1,5):
    if Dict[i][0] == 1:
        ans += 2**(i-1)
print(ans)