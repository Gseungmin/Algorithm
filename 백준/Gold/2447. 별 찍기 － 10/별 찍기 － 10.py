import sys
input = sys.stdin.readline
N = int(input())
graph = [["*"]*N for i in range(N)]

def DaC(N, x1, y1):
    if N == 1:
        return
    k = N//3
    for i in range(x1+k,x1+k*2):
        for j in range(y1+k,y1+k*2):
            graph[i][j] = " "
    DaC(k, x1, y1)
    DaC(k, x1+k, y1)
    DaC(k, x1+k*2, y1)
    DaC(k, x1, y1+k)
    DaC(k, x1+k, y1+k)
    DaC(k, x1+k*2, y1+k)
    DaC(k, x1, y1+k*2)
    DaC(k, x1+k, y1+k*2)
    DaC(k, x1+k*2, y1+k*2)
    return
DaC(N,0,0)
for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j], end = "")
    print()