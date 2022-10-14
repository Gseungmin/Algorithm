N, M = map(int,input().split())
graph = [list(input()) for i in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == "R":
            rx,ry = i,j
            graph[i][j] = "."
        elif graph[i][j] == "B":
            bx,by = i,j
            graph[i][j] = "."

ans = [11]
def DFS(rx,ry,bx,by,cnt):
    if rx == bx and ry == by:
        return
    if graph[bx][by] == "O":
        return
    if graph[rx][ry] == "O":
        ans[0] = min(ans[0], cnt)
        return
    if cnt == 10:
        return
    #N
    nrx, nbx = rx, bx
    rc, bc = 0, 0
    N = True
    while 1:
        if rc == 1 and bc == 1:
            break
        if rc == 0:
            nrx -= 1
        if bc == 0:
            nbx -= 1
        if nrx == nbx and ry == by:
            if graph[nrx][ry] == "O":
                break
            if rc == 0:
                rc = 1
                nrx += 1
            elif bc == 0:
                bc = 1
                nbx += 1
            break
        if graph[nrx][ry] == "#":
            nrx += 1
            rc = 1
        if graph[nbx][by] == "#":
            nbx += 1
            bc = 1
        if graph[nrx][ry] == "O":
            rc = 1
        if graph[nbx][by] == "O":
            bc = 1
            N = False
            break
        if nrx == nbx and ry == by:
            if graph[nrx][ry] == "O":
                break
            if rc == 0:
                nrx += 1
            if bc == 0:
                nbx += 1
            break
    if N == True:
        DFS(nrx,ry,nbx,by,cnt+1)
    #S
    nrx, nbx = rx, bx
    rc, bc = 0, 0
    S = True
    while 1:
        if rc == 1 and bc == 1:
            break
        if rc == 0:
            nrx += 1
        if bc == 0:
            nbx += 1
        if nrx == nbx and ry == by:
            if graph[nrx][ry] == "O":
                break
            if rc == 0:
                rc = 1
                nrx -= 1
            elif bc == 0:
                bc = 1
                nbx -= 1
            break
        if graph[nrx][ry] == "#":
            nrx -= 1
            rc = 1
        if graph[nbx][by] == "#":
            nbx -= 1
            bc = 1
        if graph[nrx][ry] == "O":
            rc = 1
        if graph[nbx][by] == "O":
            bc = 1
            S = False
            break
        if nrx == nbx and ry == by:
            if graph[nrx][ry] == "O":
                break
            if rc == 0:
                nrx -= 1
            if bc == 0:
                nbx -= 1
            break
    if S == True:
        DFS(nrx,ry,nbx,by,cnt+1)
    #W
    nry, nby = ry, by
    rc, bc = 0, 0
    W = True
    while 1:
        if rc == 1 and bc == 1:
            break
        if rc == 0:
            nry -= 1
        if bc == 0:
            nby -= 1
        if nry == nby and rx == bx:
            if graph[rx][nry] == "O":
                break
            if rc == 0:
                rc = 1
                nry += 1
            elif bc == 0:
                bc = 1
                nby += 1
            break
        if graph[rx][nry] == "#":
            nry += 1
            rc = 1
        if graph[bx][nby] == "#":
            nby += 1
            bc = 1
        if graph[rx][nry] == "O":
            rc = 1
        if graph[bx][nby] == "O":
            bc = 1
            W = False
            break
        if rx == bx and nry == nby:
            if graph[rx][nry] == "O":
                break
            if rc == 0:
                nry += 1
            if bc == 0:
                nby += 1
            break
    if W == True:
        DFS(rx,nry,bx,nby,cnt+1)
    #E
    nry, nby = ry, by
    rc, bc = 0, 0
    E = True
    while 1:
        if rc == 1 and bc == 1:
            break
        if rc == 0:
            nry += 1
        if bc == 0:
            nby += 1
        if nry == nby and rx == bx:
            if graph[rx][nry] == "O":
                break
            if rc == 0:
                rc = 1
                nry -= 1
            elif bc == 0:
                bc = 1
                nby -= 1
            break
        if graph[rx][nry] == "#":
            nry -= 1
            rc = 1
        if graph[bx][nby] == "#":
            nby -= 1
            bc = 1
        if graph[rx][nry] == "O":
            rc = 1
        if graph[bx][nby] == "O":
            bc = 1
            W = False
            break
        if rx == bx and nry == nby:
            if graph[rx][nry] == "O":
                break
            if rc == 0:
                nry -= 1
            if bc == 0:
                nby -= 1
            break
    if E == True:
        DFS(rx,nry,bx,nby,cnt+1)
    return
DFS(rx,ry,bx,by,0)
if ans[0] == 11:
    print(-1)
else:
    print(ans[0])