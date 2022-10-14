import sys
input = sys.stdin.readline
import copy
N, M, K = map(int,input().split())
fire = dict()
for i in range(M):
    fire[i] = list(map(int,input().split()))
#r,c,질량,속도,방향
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
for _ in range(K):
    graph = dict()
    for i in fire:
        x,y,m,s,d = fire[i]
        s %= N
        nx, ny = x, y
        for k in range(s):
            nx, ny = nx+dx[d], ny+dy[d]
            if 1<=nx<=N and 1<=ny<=N:
                continue
            else:
                if nx == 0:
                    nx = N
                elif nx == N+1:
                    nx = 1
                if ny == 0:
                    ny = N
                elif ny == N+1:
                    ny = 1
        fire[i][0] = nx
        fire[i][1] = ny
        if (nx,ny) not in graph:
            graph[(nx,ny)] = [i]
        else:
            graph[(nx,ny)].append(i)
    new_fire = dict()
    num = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if (i,j) in graph:
                if len(graph[(i,j)]) >= 2:
                    x, y = i, j
                    M = 0
                    S = 0
                    odd = 0
                    even = 0
                    cnt = len(graph[(i,j)])
                    for k in graph[(i,j)]:
                        S += fire[k][3]
                        M += fire[k][2]
                        if fire[k][4]%2 == 0:
                            even += 1
                        else:
                            odd += 1
                    M //= 5
                    S //= cnt
                    if M == 0:
                        continue
                    if even == cnt or odd == cnt:
                        d_list = [0,2,4,6]
                    else:
                        d_list = [1,3,5,7]
                    for k in range(4):
                        new_fire[num] = [x,y,M,S,d_list[k]]
                        num += 1
                else:
                    new_fire[num] = copy.deepcopy(fire[graph[(i,j)][0]])
                    num += 1
    fire = copy.deepcopy(new_fire)
ans = 0
for i in fire:
    ans += fire[i][2]
print(ans)