import sys
input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N+1)]
edge = []
for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    edge.append([a,b])

D = 0
G = 0

for i in range(1,N+1):
    if len(graph[i]) >= 3:
        k = len(graph[i])
        G += k*(k-1)*(k-2)//6
for i in edge:
    D += (len(graph[i[0]])-1)*(len(graph[i[1]])-1)
if D > G*3:
    print("D")
elif D < G*3:
    print("G")
else:
    print("DUDUDUNGA")