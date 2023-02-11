import sys
input = sys.stdin.readline
import copy
M, S = map(int,input().split())

#물고기 이동
dx = [0,-1,-1,-1,0,1,1,1,0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1,-1,-1,0,1,1,1,0,-1]

#상어 이동
s_dx = [0,-1,0,1,0]
s_dy = [0,0,-1,0,1]

#그래프 초기화
graph = dict()
for i in range(4):
    for j in range(4):
        graph[(i,j)] = 0

fish = dict()

#물고기 초기화
cnt = 1
for i in range(M):
    x, y, k = map(int,input().split())
    graph[(x-1,y-1)] += 1
    fish[cnt] = [x-1,y-1,k-1]
    cnt += 1

#상어 초기화
x, y = map(int,input().split())
shark = [x-1,y-1]

#냄새 초기화
smell = dict()
for i in range(4):
    for j in range(4):
        smell[(i,j)] = 0
        
#상어가 연속 3칸 이동 경로 함수
def DFS(x,y,route,count,fish,rd):
    if count == 3:
        
        if shark_route[0][0] == -1:
            for i in range(3):
                shark_route[0][i] = route[i]
            Max[0] = fish
        else:
            if Max[0] < fish:
                for i in range(3):
                    shark_route[0][i] = route[i]
                Max[0] = fish
            elif Max[0] == fish:
                shark_route.append(route)
                shark_route.sort()
                shark_route.pop() #사전 순 정렬
        return
    for i in range(1,5):
        nx, ny = x+s_dx[i], y+s_dy[i]
        if 0<=nx<4 and 0<=ny<4:
            route.append(i)
            rd[(nx,ny)] += 1
            if rd[(nx,ny)] == 1:
                DFS(nx,ny,route,count+1,fish+graph[(nx,ny)],rd)
            else:
                DFS(nx,ny,route,count+1,fish,rd)
            rd[(nx,ny)] -= 1
            route.pop()
    return

for _ in range(S):

    new_fish = []
    
    #모든 물고기 이동
    for i in fish:
        #물고기 이동
        x, y, k = fish[i] #x,y가 위치, k가 방향
        new_fish.append([x,y,k])
        check = False #이동가능한 방향을 찾기 위한 변수
        
        for m in range(8):
            l = k+8
            nx, ny = x+dx[l-m], y+dy[l-m]
            if 0<=nx<4 and 0<=ny<4: #격자 범위 만족
                    
                if smell[(nx,ny)] != 0: #물고기 냄새로 인해 불가능
                    continue
                if nx == shark[0] and ny == shark[1]: #상어가 있으면 불가능
                    continue
                check = True
                break
        if check == True: #물고기가 이동했을때 처리
            graph[(x,y)] -= 1
            graph[(nx,ny)] += 1
            if k-m < 0:
                fish[i] = [nx,ny,l-m]
            else:
                fish[i] = [nx,ny,k-m]

    shark_route = [[-1,-1,-1]]
    Max = [0]
    Dict = dict()
    for i in range(4):
        for j in range(4):
            Dict[(i,j)] = 0
    DFS(shark[0],shark[1],[],0,0,Dict)

    #냄새 제거
    for i in range(4):
        for j in range(4):
            if smell[(i,j)] > 0:
                smell[(i,j)] -= 1
    
    #이동하면서 물고기 삭제 및 물고기 냄새 남기기
    x, y = shark
    for i in shark_route[0]:
        d = i
        x, y = x+s_dx[d], y+s_dy[d]
        if graph[(x,y)] != 0:
            graph[(x,y)] = 0
            smell[(x,y)] = 2
        List = []
        for k in fish:
            if fish[k][0] == x and fish[k][1] == y:
                List.append(k)
        for k in List:
            fish.pop(k)
    shark = [x,y]
    
    for i in new_fish:
        x, y, k = i
        graph[(x,y)] += 1
        fish[cnt] = [x,y,k]
        cnt += 1

print(len(fish))