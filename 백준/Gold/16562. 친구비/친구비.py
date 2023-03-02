import sys
input = sys.stdin.readline
from collections import deque

#2:28
#학생이 N명, 모든 학생과 친구, i에게 돈을 주면 1달간 친구가 됨, k원이 있고 친구의 친구는 친구다
#모든 학생을 친구로 만들기

N, M, K = map(int,input().split())

money = list(map(int,input().split()))

friends = dict()
for i in range(len(money)):
    friends[i] = set()

for i in range(M):
    a, b = map(int,input().split())
    a, b = a-1, b-1
    if a == b:
        continue
    
    friends[a].add(b)
    friends[b].add(a)

import heapq

heap = []
for i in range(len(money)):
    heapq.heappush(heap,[money[i], i])

true = [False]*N

def BFS(x):
    true[x] = True
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for nx in friends[x]:
            if true[nx] == False:
                true[nx] = True
                queue.append(nx)
    return

Sum = 0
while heap:
    k, x = heapq.heappop(heap)
    if true[x] == True:
        continue
    Sum += k
    if K < Sum:
        print("Oh no")
        sys.exit()
    BFS(x)

print(Sum)