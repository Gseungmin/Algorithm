import sys
input = sys.stdin.readline
V = int(input())
graph = [[] for i in range(V+1)]
dist = [[] for i in range(V+1)]
for i in range(V-1):
    A, B, C = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
    dist[A].append(C)
    dist[B].append(C)

from collections import deque
true = [-1]*(V+1)
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