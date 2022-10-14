import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
a,b,c = graph[0][0], graph[0][1], graph[0][2]
x,y,z = graph[0][0], graph[0][1], graph[0][2]
for o in range(1,N):
    d,e,f = max(a,b) + graph[o][0], max(a,b,c) + graph[o][1], max(c,b) + graph[o][2]
    i,j,k = min(x,y) + graph[o][0], min(x,y,z) + graph[o][1], min(y,z) + graph[o][2]
    a,b,c = d,e,f
    x,y,z = i,j,k
print(max(a,b,c), min(x,y,z))