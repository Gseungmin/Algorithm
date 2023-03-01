import sys
input = sys.stdin.readline
from collections import deque
N, M, R = map(int,input().split())

graph = [list(map(int,input().split())) for i in range(N)]

def rotate(graph, x1, y1, x2, y2, new_graph, R):
    
    queue = deque()
    
    List = []
    cnt = 0
    
    for i in range(y1, y2):
        queue.append([x1,i])
        List.append([x1,i])
        cnt += 1
        
    for i in range(x1,x2):
        queue.append([i,y2])
        List.append([i,y2])
        cnt += 1
    
    for i in range(y2, y1, -1):
        queue.append([x2,i])
        List.append([x2,i])
        cnt += 1
    
    for i in range(x2,x1,-1):
        queue.append([i,y1])
        List.append([i,y1])
        cnt += 1
        
    V = R%cnt
    for i in range(V):
        queue.append(queue.popleft())
        
    for i in range(len(queue)):
        x, y = List[i]
        a, b = queue[i]
        k = graph[a][b]
        new_graph[x][y] = k
        
    nx1, ny1, nx2, ny2 = x1+1, y1+1, x2-1, y2-1
    
    if nx1 < nx2 and ny1 < ny2:
        rotate(graph, nx1, ny1, nx2, ny2, new_graph, R)
        
    return

Max = 0

new_graph = [[0]*M for i in range(N)]
rotate(graph, 0, 0, N-1, M-1, new_graph, R)
graph = new_graph

for i in range(N):
    for j in range(M):
        print(graph[i][j], end = " ")
    print()