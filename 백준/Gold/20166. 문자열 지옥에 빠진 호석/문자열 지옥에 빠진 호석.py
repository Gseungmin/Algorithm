dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,1,-1,1,-1,-1,1]
def RC(x,y,S,List):
    S += graph[x][y]
    if len(S) == len(P):
        if S == P:
            k = tuple(List)
            Dict[k] = 1
        return
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            List.append(nx)
            List.append(ny)
            RC(nx,ny,S,List)
        elif nx == -1 and 0<=ny<M:
            List.append(N-1)
            List.append(ny)
            RC(N-1,ny,S,List)
        elif nx == N and 0<=ny<M:
            List.append(0)
            List.append(ny)
            RC(0,ny,S,List)
        elif 0<=nx<N and ny == -1:
            List.append(nx)
            List.append(M-1)
            RC(nx,M-1,S,List)
        elif 0<=nx<N and ny == M:
            List.append(nx)
            List.append(0)
            RC(nx,0,S,List)
        elif nx == -1 and ny == -1:
            List.append(N-1)
            List.append(M-1)
            RC(N-1,M-1,S,List)
        elif nx == N and ny == -1:
            List.append(0)
            List.append(M-1)
            RC(0,M-1,S,List)
        elif nx == -1 and ny == M:
            List.append(N-1)
            List.append(0)
            RC(N-1,0,S,List)
        elif nx == N and ny == M:
            List.append(0)
            List.append(0)
            RC(0,0,S,List)
        List.pop()
        List.pop()
    return

N, M, K = map(int,input().split())
graph = [list(input()) for i in range(N)]
u = dict()
for i in range(K):
    P = input()
    if P in u:
        print(u[P])
        continue
    Dict = dict()
    for a in range(N):
        for b in range(M):
            if graph[a][b] == P[0]:
                List = [a,b]
                RC(a,b,"",List)
    u[P] = len(Dict)
    print(len(Dict))