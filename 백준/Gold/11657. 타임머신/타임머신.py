import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int,input().split())
edges = []
dist = [INF]*(V+1)

for i in range(E):
    u, v, w = map(int,input().split())
    edges.append([u,v,w])

def BF(start):
    dist[start] = 0
    for i in range(V):
        for j in range(E):
            node, next_node, cost = edges[j][0], edges[j][1], edges[j][2]
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                if i == V-1:
                    return True
    return False

ans = BF(1)
if ans:
    print(-1)
else:
    for i in range(2,V+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])