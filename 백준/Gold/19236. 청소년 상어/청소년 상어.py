import sys
input = sys.stdin.readline
import copy
fish = dict()
for i in range(1,17):
    fish[i] = [True]
for i in range(4):
    a, b, c, d, e, f, g, h = map(int,input().split())
    fish[a].append([i,0])
    fish[a].append(b)
    fish[c].append([i,1])
    fish[c].append(d)
    fish[e].append([i,2])
    fish[e].append(f)
    fish[g].append([i,3])
    fish[g].append(h)
shark = 0
x, y = 0, 0
for i in range(1,17):
    if fish[i][1][0] == 0 and fish[i][1][1] == 0:
        shark = i
        fish[i][0] = False
        u = fish[i][2]
        break
graph = dict()
for i in range(4):
    for j in range(4):
        graph[(i,j)] = True
graph[(0,0)] = False
dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]
Sum = [shark]
ans = [shark]
def RC(a,b,c,graph,fish,ans,Sum):
    Sum[0] = max(ans[0], Sum[0])
    graph_c = copy.deepcopy(graph)
    fish_c = copy.deepcopy(fish)
    for i in range(1,17):
        if fish_c[i][0] == False:
            continue
        k = fish_c[i][2]
        direct = k
        check = 0
        x, y = fish_c[i][1][0], fish_c[i][1][1]
        while 1:
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<4 and 0<=ny<4:
                if nx != a or ny != b:
                    if graph_c[(nx,ny)] == False:
                        graph_c[(nx,ny)] = True
                        graph_c[(x,y)] = False
                        fish_c[i][1][0] = nx
                        fish_c[i][1][1] = ny
                        check = 1
                    else:
                        for j in range(1,17):
                            if fish_c[j][1][0] == nx and fish_c[j][1][1] == ny:
                                if fish_c[j][0] == True:
                                    fish_c[i][1][0], fish_c[j][1][0] = nx, x
                                    fish_c[i][1][1], fish_c[j][1][1] = ny, y
                                    check = 1
                                    break
            if check == 1:
                fish_c[i][2] = k
                break
            k += 1
            if k == 9:
                k = 1
            if k == direct:
                break
    v = 1
    while 1:
        nx, ny = a+dx[c]*v, b+dy[c]*v
        if 0<=nx<4 and 0<=ny<4:
            if graph_c[(nx,ny)] == True:
                q = 0
                for i in range(1,17):
                    if fish_c[i][1][0] == nx and fish_c[i][1][1] == ny and fish_c[i][0] == True:
                        l = i
                        d = fish_c[i][2]
                        q = 1
                        break
                if q == 1:
                    graph_c[(nx,ny)] = False
                    ans[0] += l
                    fish_c[l][0] = False
                    RC(nx,ny,d,graph_c,fish_c,ans,Sum)
                    ans[0] -= l
                    fish_c[l][0] = True
                    graph_c[(nx,ny)] = True
        else:
            break
        v += 1
    return
RC(0,0,u,graph,fish,ans,Sum)
print(Sum[0])