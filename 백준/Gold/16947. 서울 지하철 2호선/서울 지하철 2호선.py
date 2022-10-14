import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def DFS(graph, start, prev, true, stack):
    if true[start]: #이미 방문한 정점이면
        true[0] = -1 #사이클을 찾았다고 표시
        for i in range(len(stack)-1,-1,-1):
            if stack[i] == start:
                true[start] = 2
                break
            true[stack[i]] = 2
        return
    true[start] = 1
    stack.append(start)
    for i in graph[start]:
        if i == prev:
            continue
        DFS(graph, i, start, true, stack)
        if true[0] == -1:
            return
    stack.pop(-1)
    return

def BFS(graph, start, true):
    ans = [0]*(N+1)
    check = [0]*(N+1)
    queue = []
    queue.append(start)
    check[start] = 1
    while queue:
        current = queue.pop(0)
        for i in graph[current]:
            if check[i] == 0:
                check[i] = 1
                queue.append(i)
                ans[i] = ans[current] + 1
            if true[i] == 2:
                print(ans[i], end = " ")
                return
    return

N = int(input())
graph = []
for i in range(N+1):
    graph.append([])
for i in range(N):
    A, B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

stack = []
true = [0]*(N+1)
DFS(graph, 1, 0, true, stack)

for i in range(1,N+1):
    if true[i] == 2:
        print(0, end = " ")
    else:
        BFS(graph, i, true)