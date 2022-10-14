import sys
input = sys.stdin.readline
N, E = map(int,input().split())
Graph = [] #인접 리스트
for i in range(N+1):
    Graph.append([])
for i in range(E):
    A, B = map(int,input().split())
    Graph[A].append(B)
    Graph[B].append(A)

true = [0]*(N+1)

def BFS(Graph, start, true):
    queue = []
    true[start]  = 1
    queue.append(start)
    while queue:
        current = queue.pop(0)
        for i in Graph[current]:
            if true[i] == 0:
                true[i] = 1
                queue.append(i)
    return

ans = 0
for i in range(1,N+1):
    if true[i] == 0: #방문한 적이 없으면
        BFS(Graph, i, true)
        ans += 1
print(ans)