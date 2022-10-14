def RC(x,y,k,Sum):
    if k > 1000000:
        return
    check1 = 0
    ux = x+1
    Set1 = set()
    while 0<=ux<N and graph[ux][y] == "." and true[ux][y] == -1:
        Sum -= 1
        true[ux][y] = 0
        Set1.add((ux,y))
        ux += 1
        check1 = 1
    if check1 == 1:
        RC(ux-1,y,k+1,Sum)
    for a, b in Set1:
        Sum += 1
        true[a][b] = -1
    check2 = 0
    dx = x-1
    Set2 = set()
    while 0<=dx<N and graph[dx][y] == "." and true[dx][y] == -1:
        Sum -= 1
        true[dx][y] = 0
        Set2.add((dx,y))
        dx -= 1
        check2 = 1
    if check2 == 1:
        RC(dx+1,y,k+1,Sum)
    for a, b in Set2:
        Sum += 1
        true[a][b] = -1
    check3 = 0
    uy = y+1
    Set3 = set()
    while 0<=uy<M and graph[x][uy] == "." and true[x][uy] == -1:
        Sum -= 1
        true[x][uy] = 0
        Set3.add((x,uy))
        uy += 1
        check3 = 1
    if check3 == 1:
        RC(x,uy-1,k+1,Sum)
    for a, b in Set3:
        Sum += 1
        true[a][b] = -1
    check4 = 0
    dy = y-1
    Set4 = set()
    while 0<=dy<M and graph[x][dy] == "." and true[x][dy] == -1:
        Sum -= 1
        true[x][dy] = 0
        Set4.add((x,dy))
        dy -= 1
        check4 = 1
    if check4 == 1:
        RC(x,dy+1,k+1,Sum)
    for a, b in Set4:
        Sum += 1
        true[a][b] = -1
    if check1 == 0 and check2 == 0 and check3 == 0 and check4 == 0:
        if Sum == 0:
            ans.append(k)
    return

start = 1
while 1:
    try:
        N, M = map(int,input().split())
        graph = [list(input()) for i in range(N)]
        true = [[-1]*M for i in range(N)]
        ans = []
        Sum = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] == ".":
                    Sum += 1
        for i in range(N):
            for j in range(M):
                if graph[i][j] == ".":
                    true[i][j] = 0
                    RC(i,j,0,Sum-1)
                    true[i][j] = -1
        if not ans:
            ans = -1
        else:
            ans = min(ans)
        print('Case {0}: {1}'.format(start, ans))
        start += 1
    except EOFError:
        break