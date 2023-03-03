#5:48
#진실 또는 거짓으로 말함
#되도록이면 과장, 몇 몇은 진실을 알고있음
#진실을 아는 사람이 있는 무리에서는 진실만 말함

import sys
input = sys.stdin.readline
N, M = map(int,input().split())

List = list(map(int,input().split())) #index 1부터 진실을 아는 사람들
List = List[1:]

graph = dict()
for i in range(1,N+1):
    graph[i] = set()

All = []
for i in range(M):
    party = list(map(int,input().split()))
    party = party[1:]
    
    All.append(party)
    
    #그래프 초기화
    for x in range(len(party)):
        a = party[x]
        for y in range(x+1,len(party)):
            b = party[y]
            graph[a].add(b)
            graph[b].add(a)

true = [False for i in range(N+1)]

from collections import deque

queue = deque()
for i in List:
    true[i] = True
    queue.append(i)
    
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if true[nx] == False:
            true[nx] = True
            queue.append(nx)

cnt = 0
for i in All:
    check = True
    for j in i:
        if true[j] == True:
            check = False
            break
    if check == True:
        cnt += 1

print(cnt)