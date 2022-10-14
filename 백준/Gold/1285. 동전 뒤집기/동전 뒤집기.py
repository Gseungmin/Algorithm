N = int(input())
graph = [list(input()) for i in range(N)]

def col(N, graph, x, check_t):
    for y in range(N):
        if graph[x][y] == 'T':
            graph[x][y] = 'H'
            check_t[y] -= 1
        elif graph[x][y] == 'H':
            graph[x][y] = 'T'
            check_t[y] += 1
    return

def row(N, graph, y, check_t):
    for x in range(N):
        if graph[x][y] == 'T':
            graph[x][y] = 'H'
            check_t[y] -= 1
        elif graph[x][y] == 'H':
            graph[x][y] = 'T'
            check_t[y] += 1
    return
    
check_t = []
for y in range(N):
    t = 0
    for x in range(N):
        if graph[x][y] == 'T':
            t += 1
    check_t.append(t)
    
from collections import deque    
def greedy(graph, N, x, check_t, ans):
    if x >= N:
        return
    check = deque()
    col(N, graph, x, check_t) #선택 o
    for y in range(N):
        if check_t[y] > (N//2): #t의 개수가 더 많다면
            check.append(y)
            row(N, graph, y, check_t)
    ans.append(sum(check_t))
    while check:
        row(N, graph, check.popleft(), check_t)
    greedy(graph, N, x+1, check_t, ans)
    col(N, graph, x, check_t) #선택 x
    greedy(graph, N, x+1, check_t, ans)
    return
ans = []
greedy(graph, N, 0, check_t, ans)
print(min(ans))