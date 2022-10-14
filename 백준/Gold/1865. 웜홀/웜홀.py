import sys
input = sys.stdin.readline
t = int(input())
def BF(start):
    dist[start] = 0
    for i in range(V):
        for j in edges:
            x, dx, cost = j[0], j[1], j[2]
            if dist[dx] > dist[x] + cost:
                dist[dx] = dist[x] + cost
                if i == V-1:
                    return True
    return False


for _ in range(t):
    V, E, W = map(int,input().split())
    dist = [10001]*(V+1)
    edges = []
    for i in range(E):
        u, v, w = map(int,input().split())
        edges.append([u,v,w])
        edges.append([v,u,w])
    for i in range(W):
        u, v, w = map(int,input().split())
        edges.append([u,v,-w])
    ans = BF(1)
    if ans:
        print("YES")
    else:
        print("NO")