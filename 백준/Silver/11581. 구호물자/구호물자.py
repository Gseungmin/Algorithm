import sys
input = sys.stdin.readline
N = int(input())
INF = int(1e9)
graph = [[] for i in range(N+1)]
for i in range(1,N):
    M = int(input())
    List = list(map(int,input().split()))
    for j in List:
        graph[i].append(j)
    
def DFS(x):
    if x == N:
        return
    for nx in graph[x]:
        if true[nx] == True:
            print("CYCLE")
            sys.exit()
        else:
            true[nx] = True
            DFS(nx)
            true[nx] = False
    return

true = [False]*(N+1)
true[1] = True
DFS(1)
print("NO CYCLE")