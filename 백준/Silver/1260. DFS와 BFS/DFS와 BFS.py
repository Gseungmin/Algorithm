import sys
input = sys.stdin.readline
N, E, Start = map(int,input().split())
Graph = []
for i in range(N+1):
    Graph.append([])
for i in range(E):
    A, B = map(int,input().split())
    Graph[A].append(B)
    Graph[B].append(A)
true_1 = [0]*(N+1)
true_2 = [0]*(N+1)
queue = []
for i in Graph:
    i.sort()

def DFS(Graph, Start, true):
    true[Start] = 1
    print(Start, end = " ")
    for i in Graph[Start]:
        if true[i] == 0:
            DFS(Graph, i, true)

DFS(Graph, Start, true_1)
print()
    
def BFS(Graph, Start, true, queue):
    queue.append(Start) #큐에 시작점을 넣어주고
    true[Start] = 1 #방문했다고 표시해준다.
    while queue:
        current = queue.pop(0) #가장 먼저들어간 정점을 기준으로 잡는다.
        for i in Graph[current]: #기준 정점의 연결관계를 확인한 후
            if true[i] == 0: #연결된 정점이 방문전 정점이라면
                true[i] = 1 #방문한 정점이라고 표시주고
                queue.append(i) #큐에 넣어준다.
        print(current, end = " ")
    return

BFS(Graph, Start, true_2, queue)