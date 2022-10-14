import sys
input = sys.stdin.readline
V = int(input())
List = [list(map(int,input().split())) for i in range(V)]
graph = [[] for i in range(V+1)]
dist = [[] for i in range(V+1)]
for i in List:
    j = 1
    while i[j] != -1:
        graph[i[0]].append(i[j])
        dist[i[0]].append(i[j+1])
        j += 2
true = [-1]*(V+1)
from collections import deque
queue = deque()
queue.append(1)
true[1] = 0
while queue:
    now = queue.popleft()
    for index in range(len(graph[now])):
        Next = graph[now][index]
        if true[Next] == -1:
            true[Next] = true[now] + dist[now][index]
            queue.append(Next)
            
Max = max(true)
for i in range(V+1):
    if true[i] == Max:
        start = i
        break
    
true = [-1]*(V+1)
queue = deque()
queue.append(start)
true[start] = 0
while queue:
    now = queue.popleft()
    for index in range(len(graph[now])):
        Next = graph[now][index]
        if true[Next] == -1:
            true[Next] = true[now] + dist[now][index]
            queue.append(Next)
print(max(true))